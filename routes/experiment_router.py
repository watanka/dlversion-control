from domain.experiment import experiment_crud, experiment_schema

from fastapi import APIRouter
from starlette import status


router = APIRouter(
    prefix = '/experiment'
)


@router.post('/{/create', status_code = status.HTTP_204_NO_CONTENT)
def create_experiment()