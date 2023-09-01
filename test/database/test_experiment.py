import pytest
from domain.experiment import experiment_crud
from model import Project, Model, Experiment
from sqlalchemy import select


def test_create_experiment(db_session) :
    new_experiment = experiment_crud.create_experiment(db_session, 
                                                        model_id = 1, 
                                                        project_id = 1, 
                                                        description = 'sample-experiment') 

    assert db_session.execute(select(Experiment).filter_by(modelid = 1)).scalars().one() == new_experiment

def test_delete_experiment(db_session) :
    # create
    new_experiment = experiment_crud.create_experiment(db_session, 
                                                        model_id = 1, 
                                                        project_id = 1, 
                                                        description = 'sample-experiment') 


    # delete
    experiment_crud.delete_experiment(db_session, experiment_id=1)

    assert not db_session.execute(select(Experiment)).scalars().all()
