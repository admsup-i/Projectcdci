import pytest
from app import app, APP_VERSION, PROFILE


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_renders(client):
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.get_data(as_text=True)
    assert PROFILE["name"] in body
    assert "Site Reliability Engineer" in body


def test_home_contains_experience(client):
    resp = client.get("/")
    body = resp.get_data(as_text=True)
    assert PROFILE["experience"][0]["company"] in body


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_api_profile(client):
    resp = client.get("/api/profile")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["name"] == PROFILE["name"]
    assert data["email"] == PROFILE["email"]


def test_not_found(client):
    resp = client.get("/does-not-exist")
    assert resp.status_code == 404
