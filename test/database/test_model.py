import pytest
from domain.model import model_crud
from model import Project, Model, Experiment
from sqlalchemy import select

def test_create_model(db_session) :
    new_model = model_crud.create_model(db_session,
                                        modelname = 'CRAFT',
                                        projectid = 1,
                                        description = 'scene text detection model'
                                        )
    
    assert db_session.execute(select(Model).filter_by(projectid = 1)).scalars().one() == new_model

def test_delete_model(db_session) :
    new_model = model_crud.create_model(db_session,
                                        modelname = 'CRAFT',
                                        projectid = 1,
                                        description = 'scene text detection model'
                                        )
    
    model_crud.delete_model(db_session, modelname= 'CRAFT')

    assert not db_session.scalars(select(Model)).all()