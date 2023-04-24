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
    
    @validator("citizens")
    def validate_relatives(cls, citizens):
        for citizen in citizens:
            for relative_id in citizen.relatives:
                relative_matches: list[CitizenModel] = [citizen for citizen in citizens if citizen.id == relative_id]
    
                if len(relative_matches) == 1 and citizen.id in relative_matches[0].relatives:
                    continue
                elif len(relative_matches) == 1 and citizen.id not in relative_matches[0].relatives: 
                    raise ValueError(f"Not mutual relation: Citizen {citizen.id} -> Citizen {relative_id}")
                elif len(relative_matches) == 0:
                    raise ValueError(f"Citizen with {citizen.id} ID have a relative with {relative_id} ID but there are no citizen with that ID")
                else:
                    raise ValueError(f"More multiple citizens with same ID ({relative_id})")
        return citizens
                    
                
if __name__ == '__main__':
    pass
