import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlsplit
from load_web_image import load_image


def filetype(url):
    path = urlsplit(url).path
    extension = os.path.splitext(path)[1]
    return extension


def fetch_NASA_apod_images():
    supported_extentions = ('.jpg', '.jpeg', '.png', '.gif')
    pics_number = 5
    file_dir = './images'

    url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.environ['NASA_API_KEY']
    params = {'count': pics_number, 'api_key': api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_body = response.json()

    for item_number, item in enumerate(response_body):
        image = item['url']
        extention = filetype(image)
        if extention.lower() not in supported_extentions:
            continue
        file_name = f'{file_dir}/nasa_apod_{str(item_number + 1)}{extention}'
        load_image(url=image, file_name=file_name)


def main():
    load_dotenv()
    fetch_NASA_apod_images()


if __name__ == '__main__':
    main()
