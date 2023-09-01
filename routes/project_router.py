from fastapi import APIRouter, Depends
from starlette import status

from typing import List
from domain.project import project_schema, project_crud
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter(
    prefix = '/project'
)

@router.post('/create/', response_model = project_schema.Project)
def create_project(_project : project_schema.Project,
                   db_session: Session = Depends(get_db)) :
    new_project = project_crud.create_project(db_session = db_session,
                                projectname = _project.projectname,
                                description = _project.description
                                )

    return new_project

@router.get('/', response_model = List[project_schema.Project])
def list_projects(db_session: Session = Depends(get_db)) :
    return project_crud.list_projects(db_session)

