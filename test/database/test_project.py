import pytest
from domain.project import project_crud
from model import Project, Model, Experiment
from sqlalchemy import select

def test_create_project(db_session) :
    new_project = project_crud.create_project(db_session,
                                              projectname = 'CLOVA',
                                              description = 'hyperclova',
                                            )
    
    assert db_session.execute(select(Project).filter_by(projectname = 'CLOVA')).scalars().one() == new_project

def test_delete_project(db_session) :

    new_project = project_crud.create_project(db_session,
                                              projectname = 'CLOVA',
                                              description = 'hyperclova',
                                            )
    
    project_crud.delete_project(db_session, projectname = 'CLOVA')

    assert not db_session.execute(select(Project)).scalars().all()