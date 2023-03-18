import re
import datetime
from typing import Literal
from pydantic import BaseModel, constr, validator

import citizen_analyzer.settings as settings


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
        datetime.datetime.strptime(value, settings.DATE_PATTERN)
        return value


class Import(BaseModel):
    citizens: list[Citizen]


if __name__ == '__main__':
    pass
