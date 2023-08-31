from sqlalchemy.orm import Session
from model import Experiment

def create_experiment(db_session : Session, modelid, projectid, description) :
    new_experiment = Experiment(
                            modelid = modelid,
                            projectid = projectid,
                            description = description
                    )

    db_session.query(Experiment).add(new_experiment)
    db_session.commit()