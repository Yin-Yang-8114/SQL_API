import requests
from SQL_API.client.config import SERVER_URL


def get_data(endpoint, params=None):
    url = SERVER_URL + endpoint

    response = requests.get(url,
        params=params,
        timeout=10,)
    response.raise_for_status()
    return response.json()


def post_data(endpoint, data):
    url = SERVER_URL + endpoint

    response = requests.post(
        url,
        json=data,
        timeout=10,)
    response.raise_for_status()
    return response.json()