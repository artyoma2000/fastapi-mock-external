import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from main import app, fetch_external_data, write_to_database
import httpx

client = TestClient(app)


def test_get_data_success():
    with patch('main.fetch_external_data', new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = {"key": "value"}

        response = client.get("/data")
        assert response.status_code == 200
        assert response.json() == {"key": "value"}


def test_get_data_failure():
    with patch('main.fetch_external_data', new_callable=AsyncMock) as mock_fetch:
        mock_fetch.side_effect = httpx.HTTPStatusError(
            message="Error",
            request=None,
            response=httpx.Response(status_code=404)
        )

        response = client.get("/data")
        assert response.status_code == 404


def test_post_to_db_success():
    with patch('main.write_to_database', new_callable=AsyncMock) as mock_write:
        response = client.post("/db", json={"key": "value"})
        assert response.status_code == 200
        assert response.json() == {"status": "success"}


def test_post_to_db_failure():
    with patch('main.write_to_database', new_callable=AsyncMock) as mock_write:
        mock_write.side_effect = ValueError("No data provided")

        response = client.post("/db", json={})
        assert response.status_code == 400
