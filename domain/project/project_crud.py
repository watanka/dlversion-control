from sqlalchemy.orm import Session
from model import Project

def list_projects(db_session : Session) :
    return db_session.query(Project).all()