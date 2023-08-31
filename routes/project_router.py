from fastapi import APIRouter

router = APIRouter(
    prefix = '/project'
)

@router.get('/')
def list_projects() :
    return 