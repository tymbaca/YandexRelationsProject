import json
import random
from pprint import pprint
from typing import TypeAlias
from mimesis import Person, Address
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender

import tests.settings as settings
from citizen_analyzer.api.pydantic_models import Import, Citizen
import tests.utils as utils

IDsDict: TypeAlias = dict[int, set[int]]

# Initialising test data generators
person_generator = Person(settings.TEST_DATA_LANGUAGE)
address_generator = Address(settings.TEST_DATA_LANGUAGE)
extra_info_generator = RussiaSpecProvider()


class ImportGenerator:
    def generate_import(self, citizen_count: int, relative_max_count: int = 3) -> Import:
        """Генерирует Pydantic модель импорта со случайными гражданами."""
        citizens = []
        ids_dict = self._generate_ids_dict(citizen_count, relative_max_count)
        for citizen_id, relatives in ids_dict.items():
            citizen = self._generate_citizen(citizen_id, relatives)
            citizens.append(citizen)
        return Import(citizens=citizens)

    @staticmethod
    def _generate_citizen(citizen_id, relatives: set[int]) -> Citizen:
        """Создает Pydantic модель гражданина со случайными данными."""
        # Selecting random gender. Need to be one gender for one citizen.
        gender: Gender = random.choice(list(Gender))
        return Citizen(
            citizen_id=citizen_id,
            town=address_generator.city(),
            street=address_generator.street_name(),
            building=address_generator.street_number(),
            apartment=random.randint(1, 320),
            name=f"{person_generator.last_name(gender)} {person_generator.name(gender)} {extra_info_generator.patronymic(gender)}",
            birth_date=utils.random_date().strftime(settings.DATE_PATTERN),
            gender=gender.value,  # Code smell… We are not sure that gender.value and API genders will be the same in future
            relatives=relatives)

    @staticmethod
    def _generate_ids_dict(count: int, relatives_max_count: int) -> IDsDict:
        """Генерирует словарь с id родственных связей."""
        ids_dict: IDsDict = dict()
        ids = tuple(range(count))

        for id in ids:
            ids_dict[id] = set()

        for citizen_id in ids:
            for _ in range(random.randint(0, relatives_max_count)):
                # Skip if already have enough relatives
                if len(ids_dict[citizen_id]) >= relatives_max_count:
                    continue

                # Removing current id from target list
                ids_without_current = [id for id in ids if id != citizen_id]
                if len(ids_without_current) > 0:
                    relative_id = random.choice(ids_without_current)

                    # Add ids in both citizen and relative
                    ids_dict[citizen_id].add(relative_id)
                    ids_dict[relative_id].add(citizen_id)

        return ids_dict

    @staticmethod
    def save_import_to_file(import_model: Import = None, path: str = "import.json") -> None:
        with open(path, "w") as f:
            import_json = json.dumps(import_model.dict(), ensure_ascii=False)
            f.write(import_json)


if __name__ == '__main__':
    import_generator = ImportGenerator()
    import_model = import_generator.generate_import(1)
    import_generator.save_import_to_file(import_model)
