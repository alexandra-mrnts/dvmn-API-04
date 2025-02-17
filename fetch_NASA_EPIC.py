import os
import requests
import datetime
import configargparse
from pathlib import Path
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from load_web_image import load_image


DEFAULT_STORAGE_DIR = 'images'
DEFAULT_PICS_NUMBER = 3


def fetch_NASA_EPIC_images(max_pics_number, storage_dir, api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_body = response.json()

    for image_number, image in enumerate(response_body, start=1):
        if image_number > max_pics_number:
            return
        image_name = image['image']
        image_date = datetime.datetime.fromisoformat(image['date'])
        image_date = image_date.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png'
        file_name = storage_dir.joinpath(f'nasa_EPIC_{image_number}.png')
        load_image(url=image_url, query_params=params, file_name=file_name)


def main():
    load_dotenv()
    parser = configargparse.ArgParser()
    parser.add_argument('-d',
                        '--directory',
                        env_var='NASA_EPIC_STORAGE_DIR',
                        default=DEFAULT_STORAGE_DIR)
    parser.add_argument('-n',
                        '--pics_number',
                        env_var='NASA_EPIC_PICS_NUMBER',
                        default=DEFAULT_PICS_NUMBER)
    args = parser.parse_args()
    storage_dir = Path(args.directory).resolve()
    max_pics_number = int(args.pics_number)
    api_key = os.environ['NASA_API_KEY']
    try:
        fetch_NASA_EPIC_images(max_pics_number=max_pics_number,
                            storage_dir=storage_dir,
                            api_key=api_key)
    except HTTPError as err:
        if err.response.status_code == 403:
            print('Ошибка. Неверный API KEY.')
        else:
            print(f'Возникла ошибка: {err}')


if __name__ == '__main__':
    main()
