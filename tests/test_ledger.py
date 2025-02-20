import os
import sys

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add core folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app1.src.main import app
from core.database import Base, get_db

TEST_DATABASE_URL = "postgresql://user:password@localhost/test_db"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(test_db):
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


def test_initial_balance(client):
    response = client.get("/ledger/user1")
    assert response.status_code == 200
    assert response.json()["balance"] == 0


def test_create_entry(client):
    response = client.post(
        "/ledger",
        json={
            "owner_id": "user1",
            "operation": "SIGNUP_CREDIT",
            "amount": 3,
            "nonce": "abc123",
            "created_on": "2024-05-20T12:00:00",
        },
    )
    assert response.status_code == 200


def test_duplicate_nonce(client):
    client.post(
        "/ledger",
        json={
            "owner_id": "user1",
            "operation": "CREDIT_ADD",
            "amount": 10,
            "nonce": "unique123",
            "created_on": "2024-05-20T12:00:00",
        },
    )
    response = client.post(
        "/ledger",
        json={
            "owner_id": "user1",
            "operation": "CREDIT_SPEND",
            "amount": 1,
            "nonce": "unique123",
            "created_on": "2024-05-20T12:01:00",
        },
    )
    assert response.status_code == 400
    assert "Duplicate nonce" in response.text


def test_insufficient_balance(client):
    response = client.post(
        "/ledger",
        json={
            "owner_id": "user2",
            "operation": "CREDIT_SPEND",
            "amount": 1,
            "nonce": "new123",
            "created_on": "2024-05-20T12:00:00",
        },
    )
    assert response.status_code == 400
