from sqlalchemy.orm import Session
from sqlalchemy import select
from model import Experiment

def create_experiment(db_session : Session, model_id, project_id, description = None) :
    new_experiment = Experiment(
                            modelid = model_id,
                            projectid = project_id,
                            description = description
                    )

    db_session.add(new_experiment)
    db_session.commit()

    return new_experiment

def delete_experiment(db_session : Session, experiment_id) :

    db_experiment = db_session.get(Experiment, experiment_id)

    if db_experiment :
        db_session.delete(db_experiment)
        db_session.commit()
    else :
        raise ValueError(f'experiment {experiment_id} not found')
