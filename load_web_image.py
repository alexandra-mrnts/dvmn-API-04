import requests
from pathlib import Path


def load_image(url, file_name, query_params=None):
    response = requests.get(url, query_params)
    response.raise_for_status()
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)
    with open(file_name, 'wb') as file:
        file.write(response.content)
