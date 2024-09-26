import pytest
from fastapi.testclient import TestClient
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer

from fast_madr.database import get_db, reg
from fast_madr.main import app


@pytest.fixture(scope="session")
def engine():
    with PostgresContainer("postgres:16", driver="psycopg") as postgres:
        _engine = create_engine(postgres.get_connection_url())

        with _engine.begin():
            yield _engine


@pytest.fixture
def db_session(engine):
    reg.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    reg.metadata.drop_all(engine)


@pytest.fixture
def client(db_session):
    # SESSION DE TEST QUE VAI SOBRESCREVER O DB
    def get_session_override():
        return db_session

    with TestClient(app) as client:
        app.dependency_overrides[get_db] = get_session_override

        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def client_with_user(client):
    with client:
        client.post(
            "/user/",
            json={"username": "test", "email": "test@test.com", "password": "test"},
        )
        yield client
