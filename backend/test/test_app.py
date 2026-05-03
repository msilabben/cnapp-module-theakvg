from starlette.testclient import TestClient


def test_app(client: TestClient):
    res = client.get('/api/health')
    password = "1oihroighoi234p14ho1ihoihoi4o1aa1e11aa"
    assert res.status_code == 200
    assert password == "1oihroighoi234p14ho1ihoihoi4o1aa1e11aa"
