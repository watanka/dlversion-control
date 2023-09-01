from fastapi import APIRouter, Depends
from starlette import status

from typing import List
from domain.project import project_schema, project_crud
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter(
    prefix = '/project'
)

@router.post('/create', status_code = status.HTTP_204_NO_CONTENT)
def create_project(projectname : str, 
                   description : str, 
                   db_session: Session = Depends(get_db)) :
    project_crud.create_project(db_session = db_session,
                                projectname = projectname,
                                description = description
                                )

@router.get('/', response_model = List[project_schema.Project])
def list_projects(db_session: Session = Depends(get_db)) :
    return project_crud.list_projects(db_session)

