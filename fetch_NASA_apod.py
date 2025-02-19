import os
import requests
import configargparse
from pathlib import Path
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from urllib.parse import urlsplit
from load_web_image import load_image


SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')
DEFAULT_STORAGE_DIR = 'images'
DEFAULT_PICS_NUMBER = 3


def get_filetype(url):
    path = Path(urlsplit(url).path)
    return path.suffix


def fetch_NASA_apod_images(pics_number, storage_dir, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'count': pics_number, 'api_key': api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_body = response.json()

    for image_number, image in enumerate(response_body, start=1):
        image_url = image['url']
        extension = get_filetype(image_url)
        if extension.lower() not in SUPPORTED_EXTENSIONS:
            continue
        filepath = storage_dir.joinpath(f'nasa_apod_{image_number}{extension}')
        load_image(url=image_url, filepath=filepath)


def main():
    load_dotenv()
    parser = configargparse.ArgParser()
    parser.add_argument('-d',
                        '--directory',
                        env_var='NASA_APOD_STORAGE_DIR',
                        default=DEFAULT_STORAGE_DIR)
    parser.add_argument('-n',
                        '--pics_number',
                        type=int,
                        env_var='NASA_APOD_PICS_NUMBER',
                        default=DEFAULT_PICS_NUMBER)
    args = parser.parse_args()
    
    storage_dir = Path(args.directory).resolve()
    pics_number = args.pics_number
    api_key = os.getenv('NASA_API_KEY')
    try:
        fetch_NASA_apod_images(pics_number=pics_number,
                               storage_dir=storage_dir,
                               api_key=api_key)
    except HTTPError as err:
        if err.response.status_code == 403:
            print('Ошибка. Неверный API KEY.')
        else:
            print(f'Возникла ошибка: {err}')
        

if __name__ == '__main__':
    main()
