import re
import datetime
from typing import Literal
from pydantic import BaseModel, constr, validator


DATE_PATTERN = "%d.%m.%Y"

# region tests
with open('../../tests/citizen.json') as f:
    test_citizen = f.read()

# endregion


class TestModel(BaseModel):
    id: int
    name: str


class Citizen(BaseModel):
    citizen_id: int
    town: str
    street: str
    building: str
    apartment: int
    name: str
    birth_date: str
    gender: str
    relatives: list[int]

    @validator("birth_date")
    def validate_birthdate(cls, value):
        datetime.datetime.strptime(value, DATE_PATTERN)
        return value


class Import(BaseModel):
    citizens: list[Citizen]


if __name__ == '__main__':
    result = Citizen.parse_raw(test_citizen)
    # TestModel.parse_raw(test_model)
