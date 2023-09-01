import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from fastapi.testclient import TestClient

from main import app

@pytest.fixture()
def db_session() :
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind = engine, autoflush = False, autocommit = False)
    db = session()
    yield db
    db.rollback()
    db.close()


@pytest.fixture()
def testclient(db_session) :
    def get_test_db() :
        return db_session

    client = TestClient(app)
    app.dependency_overrides[get_db] = get_test_db

    return client