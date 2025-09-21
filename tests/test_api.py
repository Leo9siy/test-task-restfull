import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_list_update_delete_task():
    try:
        # Используем асинхронный клиент
        async with AsyncClient( base_url="http://test") as client:

            # Create
            r = await client.post("/tasks", json={"title": "Write tests"})
            assert r.status_code == 201
            task = r.json()
            assert task["title"] == "Write tests"
            tid = task["id"]

            # List
            r = await client.get("/tasks")
            assert r.status_code == 200
            items = r.json()
            assert any(t["id"] == tid for t in items)

            # Update
            r = await client.put(f"/tasks/{tid}", json={"is_done": True})
            assert r.status_code == 200
            assert r.json()["is_done"] is True

            # Delete
            r = await client.delete(f"/tasks/{tid}")
            assert r.status_code == 204

            # 404 on update after delete
            r = await client.put(f"/tasks/{tid}", json={"is_done": False})
            assert r.status_code == 404
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")