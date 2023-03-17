from mimesis import Person
from mimesis.builtins import RussiaSpecProvider
from citizen_analyzer.api.pydantic_models import Import, Citizen


def generate_import(count: int):
    pass


def create_citizen(id, relatives) -> Citizen:
    citizen = Citizen()
    pass
    # citizen_id=
    # town: str
    # street: str
    # building: str
    # apartment: int
    # name: str
    # birth_date: str
    # gender: str
    # relatives: list[int])


def generate_ids_dict(count, relatives_max) -> dict[int, set[int]]:
    pass
