from pydantic import BaseModel
class UserRequest(BaseModel):
    username: str
    password: str

class StrikeRequest(UserRequest):
    strike_asset_id: int | None = None
    name: str | None = None
