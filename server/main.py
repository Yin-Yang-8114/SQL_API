from fastapi import FastAPI, HTTPException
from SQL_API.server.database import db
from SQL_API.server.service import find_lowest_readiness
from SQL_API.server.auth import register_user, check_user
from SQL_API.server.schemas import UserRequest, SearchRequest
app = FastAPI()

@app.get("/tables")
def show_tables():
    with db.connection_context():
        cursor = db.execute_sql("SHOW TABLES;")
        rows = cursor.fetchall()
    return {"tables": [row[0] for row in rows]}


@app.get("/devices/lowest-readiness")
def get_lowest_readiness(
    device_id: int | None = None,
    device_name: str | None = None,):
    if device_id is not None and device_name is not None:
        raise HTTPException(
            status_code=400,
            detail="Send either device_id or device_name, not both",)

    if device_id is not None:
        if device_id <= 0:
            raise HTTPException(
                status_code=400,
                detail="Device ID must be greater than zero",)

        result = find_lowest_readiness("id", device_id)

    elif device_name is not None:
        device_name = device_name.strip()

        if not device_name:
            raise HTTPException(
                status_code=400,
                detail="Device name cannot be empty",)
        result = find_lowest_readiness("name", device_name)

    else:
        raise HTTPException(
            status_code=400,
            detail="Send device_id or device_name",)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="No matching device data in active stations",)
    return result

@app.post("/register", status_code=201)
def register(request: UserRequest):
    return register_user(request.username, request.password)


@app.post("/devices/lowest-readiness/secure")
def secure_search(request: SearchRequest):
    if not check_user(request.username, request.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    return get_lowest_readiness(
        device_id=request.device_id,
        device_name=request.device_name,
    )