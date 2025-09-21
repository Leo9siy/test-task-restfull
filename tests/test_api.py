from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


async def test_create_list_update_delete_task():
    r = client.post("/tasks", json={"title": "Write tests"})
    assert r.status_code == 201
    task = r.json()
    assert task["title"] == "Write tests"
    tid = task["id"]


    # list
    r = client.get("/tasks")
    assert r.status_code == 200
    items = r.json()
    assert any(t["id"] == tid for t in items)


    # update
    r = client.put(f"/tasks/{tid}", json={"is_done": True})
    assert r.status_code == 200
    assert r.json()["is_done"] is True


    # delete
    r = client.delete(f"/tasks/{tid}")
    assert r.status_code == 204


    # 404 on update after delete
    r = client.put(f"/tasks/{tid}", json={"is_done": False})
    assert r.status_code == 404
