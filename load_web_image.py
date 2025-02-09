import requests
from pathlib import Path


def load_image(url, file_name):
    response = requests.get(url)
    response.raise_for_status()
    Path(file_name).parent.mkdir(exist_ok=True)
    with open(file_name, 'wb') as file:
        file.write(response.content)
