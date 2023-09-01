import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database import Base

@pytest.fixture()
def db_session() :
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind = engine, autoflush = False, autocommit = False)
    db = session()
    yield db
    db.rollback()
    db.close()
