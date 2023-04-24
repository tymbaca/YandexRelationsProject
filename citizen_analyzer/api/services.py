from sqlalchemy.orm import Session

from citizen_analyzer.api import pydantic_models
from citizen_analyzer.db import models
from citizen_analyzer.app import app

def handle_import_and_return_id(import_model: pydantic_models.ImportModel) -> None:
    with Session(app.database_engine) as session:
        db_import = models.Import()
        session.add(db_import)
        
        for citizen in import_model.citizens:
            db_citizen = models.Citizen(id=citizen.id,
                                        import_id=db_import.id,
                                        town=citizen.town,
                                        street=citizen.street,
                                        building=citizen.building,
                                        apartment=citizen.apartment,
                                        name=citizen.name,
                                        birthdate=citizen.birthdate,
                                        gender=citizen.gender)
            session.add(db_citizen)
            
            for relative_id in citizen.relatives:
                relation = models.Relation(import_id=db_import.id, citizen_id=citizen.id, relative_id=relative_id)
                session.add(relation)

        session.commit()
        return db_import.id


