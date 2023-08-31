from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel) :
    projectname : str
    description : str
    created_at : datetime

    
