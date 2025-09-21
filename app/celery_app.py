from datetime import datetime
from pathlib import Path

import httpx
import pandas as pd
from celery import Celery


celery = Celery('tasks', broker='redis://redis:6379/0')

USERS_URL = "https://jsonplaceholder.typicode.com/users"
DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "users.csv"

@celery.task
async def fetch_and_save_users():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(USERS_URL)
        resp.raise_for_status()
        users = resp.json()
    rows = [{"id": u["id"], "name": u["name"], "email": u["email"]} for u in users]
    df = pd.DataFrame(rows, columns=["id", "name", "email"])
    df.to_csv(CSV_PATH, index=False)
    return {"saved": len(df), "path": str(CSV_PATH), "ts": datetime.utcnow().isoformat()}
