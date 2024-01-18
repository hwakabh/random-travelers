from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_url_notfound():
    resp = client.get('/no_exist')
    # FastAPI default
    rbody = {"detail": "Not Found"}

    assert resp.status_code == 404
    assert resp.json() == rbody


def test_healthz():
    resp = client.get('/healthz')
    rbody = {"status": "ok"}
    assert resp.status_code == 200
    assert resp.json() == rbody
