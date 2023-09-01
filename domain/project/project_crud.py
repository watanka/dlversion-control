from sqlalchemy.orm import Session
from sqlalchemy import select
from model import Project, Model, Experiment

def list_projects(db_session : Session) :
    return db_session.execute(select(Project)).scalars().all()

def create_project(db_session : Session, projectname, description) :
    new_project = Project(projectname = projectname,
                          description = description,
                          )

    db_session.add(new_project)
    db_session.commit()

    return new_project

def delete_project(db_session, projectname) : 

    db_project = db_session.execute(
                                    select(Project).
                                    filter_by(projectname = projectname)
                                    ).scalar_one()
    
    if db_project :
        db_session.delete(db_project)
        db_session.commit()
    else :
        raise ValueError(f'project {projectname} not found')