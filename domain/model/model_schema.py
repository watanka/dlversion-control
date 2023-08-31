from pydantic import BaseModel

class Model(BaseModel) :
    projectname : str
    description : str | None