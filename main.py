from fastapi import FastAPI, HTTPException
from typing import Any
import httpx

app = FastAPI()

# Функция для получения данных из внешнего API
async def fetch_external_data() -> Any:
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com/data')
        response.raise_for_status()
        return response.json()

# Функция для записи данных в базу данных
async def write_to_database(data: Any) -> None:
    if not data:
        raise ValueError("No data provided")
    # Фиктивная операция записи
    print("Data written to database")

@app.get("/data")
async def get_data():
    try:
        data = await fetch_external_data()
        return data
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=str(exc))
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.post("/db")
async def post_to_db(data: dict):
    try:
        await write_to_database(data)
        return {"status": "success"}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
