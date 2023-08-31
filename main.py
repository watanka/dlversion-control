from fastapi import FastAPI
from routes import project_router, model_router, experiment_router
app = FastAPI()


@app.get('/ping')
def healthcheck() :
    return 'pong'

app.include_router(project_router.router)
app.include_router(model_router.router)
app.include_router(experiment_router.router)