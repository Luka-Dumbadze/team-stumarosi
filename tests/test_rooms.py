from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_existing_room_returns_data():  # AC2
    r = client.get("/rooms/101")
    assert r.status_code == 200
    data = r.json()
    assert data["room_number"] == 101
    assert data["guest_name"] == "Nino Beridze"
    assert data["status"] == "occupied"

def test_nonexistent_room_returns_422_with_error_shape():  # AC3
    r = client.get("/rooms/999")
    assert r.status_code == 422
    assert r.json() == {
        "error": "Room 999 does not exist in registry",
        "field": "room_number"
    }

def test_invalid_room_format_returns_422_with_field():  # AC3
    r = client.get("/rooms/abc")
    assert r.status_code == 422
    assert set(r.json()) == {"error", "field"}
    assert r.json()["field"] == "room_number"