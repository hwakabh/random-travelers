from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_healthz_ok():
    resp = client.get('/healthz')
    assert resp.status_code == 200


def test_index_ok():
    resp = client.get('/api/v1/')
    assert resp.status_code == 200


def test_index_response():
    resp = client.get('/api/v1/')
    rbody = {
      "path": "/api/v1/",
      "detail": "v1 API root"
    }
    assert resp.json() == rbody


def test_fetch_ok():
    resp = client.get('/api/v1/fetch')
    assert resp.status_code == 200
