import json
import re
import datetime
from typing import Literal
from pydantic import BaseModel, constr, validator

import citizen_analyzer.settings as settings


class CitizenModel(BaseModel):
    id: int
    town: str
    street: str
    building: str
    apartment: int
    name: str
    birth_date: str
    gender: str
    relatives: list[int]

    @validator("birth_date")
    def validate_birth_date(self, value):
        datetime.datetime.strptime(value, settings.DATE_PATTERN)
        return value


class ImportModel(BaseModel):
    citizens: list[CitizenModel]

    def json(self):
        import_dict: dict = self.dict()
        import_json = json.dumps(import_dict, ensure_ascii=False)
        return import_json


if __name__ == '__main__':
    pass
