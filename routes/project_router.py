from fastapi import APIRouter, Depends
from domain.project import project_schema, project_crud
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter(
    prefix = '/project'
)

@router.get('/', response_model = project_schema.Project)
def list_projects(db_session: Session = Depends(get_db)) :
    return project_crud.list_projects(db_session)
    