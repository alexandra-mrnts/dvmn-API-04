import requests
from pathlib import Path


def load_image(url, filepath, query_params=None):
    response = requests.get(url, query_params)
    response.raise_for_status()
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'wb') as file:
        file.write(response.content)
