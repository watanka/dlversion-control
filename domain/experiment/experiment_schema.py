from pydantic import BaseModel

class Experiment(BaseModel) :
    modelname : str
    description : str | None