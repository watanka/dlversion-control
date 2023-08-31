from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

DB_URL = 'sqlite:///./dlversion.db'

engine = create_engine(DB_URL, connect_args = {'check_same_thread' : False})
session = sessionmaker(bind = engine, autocommit = False, autoflush = False)

Base = declarative_base()

def get_db() :
    db = session()
    try :
        yield db
    finally :
        db.close()
