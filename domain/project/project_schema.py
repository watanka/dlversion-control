from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Project(BaseModel) :
    model_config = ConfigDict(from_attributes=True)
    # id : int
    projectname : str
    description : str | None
    # created_at : datetime | None

    
