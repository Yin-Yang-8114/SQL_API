from pydantic import BaseModel
class UserRequest(BaseModel):
    username: str
    password: str

class SearchRequest(UserRequest):
    device_id: int | None = None
    device_name: str | None = None