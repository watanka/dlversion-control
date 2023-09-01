from sqlalchemy.orm import Session
from sqlalchemy import select
from model import Model

def create_model(db_session : Session, modelname, projectid, description) :
    new_model = Model(
                        modelname = 'CRAFT',
                        projectid = 1,
                        description = 'scene text detection model'
                   )
    db_session.add(new_model)
    db_session.commit()
    return new_model

def delete_model(db_session : Session, modelname) : 

    db_model = db_session.execute(
                                select(Model).
                                filter_by(modelname=modelname)
                                ).scalar_one()
    
    if db_model :
        db_session.delete(db_model)
        db_session.commit()
    else :
        raise ValueError(f'model {modelname} not found')