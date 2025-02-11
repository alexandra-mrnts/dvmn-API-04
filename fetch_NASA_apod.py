import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlsplit
from load_web_image import load_image


SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')
FILE_DIR = './images'
DEFAULT_PICS_NUMBER = 5


def file_type(url):
    path = urlsplit(url).path
    extension = os.path.splitext(path)[1]
    return extension


def fetch_NASA_apod_images():
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.environ['NASA_API_KEY']
    try:
        pics_number = int(os.environ['NASA_APOD_PICS_NUMBER'])
    except KeyError:
        pics_number = DEFAULT_PICS_NUMBER
    params = {'count': pics_number, 'api_key': api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_body = response.json()

    for image_number, image in enumerate(response_body):
        image_url = image['url']
        extension = file_type(image_url)
        if extension.lower() not in SUPPORTED_EXTENSIONS:
            continue
        file_name = f'{FILE_DIR}/nasa_apod_{str(image_number + 1)}{extension}'
        load_image(url=image_url, file_name=file_name)


def main():
    load_dotenv()
    fetch_NASA_apod_images()


if __name__ == '__main__':
    main()
