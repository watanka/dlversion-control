from pydantic import BaseModel, ConfigDict

class Model(BaseModel) :
    model_config = ConfigDict(from_attributes=True)
    projectname : str
    description : str | None