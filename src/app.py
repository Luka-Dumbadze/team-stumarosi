import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI(title="StumarOSI Triage Service")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "rooms.json"

def load_rooms() -> list[dict]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# RequestValidationError Handler: {"error": ..., "field": ...}
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    first_error = errors[0] if errors else {}
    field = first_error.get("loc", ["unknown"])[-1]
    return JSONResponse(
        status_code=422,
        content={"error": f"Invalid input for field '{field}'", "field": str(field)}
    )

# HTTPException Handler: აბრუნებს პირდაპირ error shape-ს "detail"-ის გარეშე
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, dict):
        return JSONResponse(status_code=exc.status_code, content=exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc.detail), "field": "unknown"}
    )

@app.get("/rooms/{room_number}")
def get_room(room_number: int):
    rooms = load_rooms()
    room = next((r for r in rooms if r["room_number"] == room_number), None)
    if not room:
        raise HTTPException(
            status_code=422,
            detail={"error": f"Room {room_number} does not exist in registry", "field": "room_number"}
        )
    return room
