from pydantic import BaseModel, ConfigDict

class Experiment(BaseModel) :
    model_config = ConfigDict(from_attributes=True)
    modelname : str
    description : str | None