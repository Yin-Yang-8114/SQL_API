import requests
from config import SERVER_URL

def request_last_location(search_type: str, search_value) -> dict:
    if search_type == "id":
        params = {"target_id": search_value}
    elif search_type == "name":
        params = {"name": search_value}
    else:
        raise ValueError("Search type must be id or name")
    url = SERVER_URL + "/targets/last-location"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()