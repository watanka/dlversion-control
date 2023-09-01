from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from routes import project_router, model_router, experiment_router
from error_handler import validation_exception_handler
app = FastAPI()


@app.get('/ping')
def healthcheck() :
    return 'pong'

app.include_router(project_router.router)
app.include_router(model_router.router)
app.include_router(experiment_router.router)

# app.add_exception_handler(ResponseValidationError, validation_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

