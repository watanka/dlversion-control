from model import Project
from database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app

# setting db
DB_URL = 'sqlite:///./test.db'
engine = create_engine(DB_URL, connect_args={'check_same_thread' : False})
TestingSessionLocal = sessionmaker(bind = engine, autoflush=False, autocommit = False)
Base.metadata.create_all(bind = engine)

def override_get_db() :
    try :
        db = TestingSessionLocal()
        yield db
    finally :
        db.close()

## setting api server
testclient = TestClient(app)
app.dependency_overrides[get_db] = override_get_db


def test_list_projects() :
    new_project = Project(projectname = 'CLOVA',
                          description = 'building scene text detection'
                          )

    response = testclient.get('/project/')

    assert response.status_code == 200
    data = response.json()

def test_create_project() :
    new_project = Project(projectname = 'CLOVA',
                          description = 'building scene text detection'
                          )
    
    response = testclient.post('/project/create/',
                    json = {
                        'projectname' : new_project.projectname,
                        'description' : new_project.description
                    }
                )
    
    assert response.status_code == 204 # No response
    data = response.json()

    assert data['projectname'] == new_project.projectname
    assert data['description'] == new_project.description



    