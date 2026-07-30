import pytest
from app import app, APP_VERSION


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["message"] == "Hello from the CI/CD demo app! iliyas Siddiqui, this application is hosted on k8s"
    assert data["version"] == APP_VERSION


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_add(client):
    resp = client.get("/add/2/3")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["result"] == 5


def test_add_negative(client):
    resp = client.get("/add/-4/10")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["result"] == 6


def test_not_found(client):
    resp = client.get("/does-not-exist")
    assert resp.status_code == 404
