from fastapi import FastAPI, HTTPException
from target_service import find_last_location

app = FastAPI()


@app.get("/targets/last-location")
def get_last_location(
    target_id: int | None = None,name: str | None = None,):
    if target_id is not None and name is not None:
        raise HTTPException(status_code=400,detail="Send either target_id or name, not both")

    if target_id is not None:
        if target_id <= 0:
            raise HTTPException( status_code=400, detail="Target ID must be greater than zero",)
        result = find_last_location("id", target_id)
    elif name is not None:
        name = name.strip()
        if not name:
            raise HTTPException(status_code=400,detail="Target name cannot be empty",)
        result = find_last_location("name", name)
    else:
        raise HTTPException(status_code=400,detail="Send target_id or name",)
    if result is None:
        raise HTTPException(status_code=404,detail="Target not found",)
    return result