import requests
import configargparse
from pathlib import Path
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from load_web_image import load_image


DEFAULT_STORAGE_DIR = 'images'


def fetch_spacex_launch_images(storage_dir, launch_id):
    url_template = 'https://api.spacexdata.com/v5/launches/'
    url = f'{url_template}{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    response_body = response.json()
    images = response_body['links']['flickr']['original']
    for image_number, image in enumerate(images, start=1):
        filepath = storage_dir.joinpath(f'spacex_{image_number}.jpg')
        load_image(url=image, filepath=filepath)


def main():
    load_dotenv()

    parser = configargparse.ArgParser()
    parser.add_argument('-l',
                        '--launch_id',
                        default='latest')
    parser.add_argument('-d',
                        '--directory',
                        env_var='SPACEX_STORAGE_DIR',
                        default=DEFAULT_STORAGE_DIR)
    args = parser.parse_args()

    storage_dir = Path(args.directory).resolve()
    launch_id = args.launch_id

    try:
        fetch_spacex_launch_images(storage_dir=storage_dir,
                                   launch_id=launch_id)
    except HTTPError as err:
        if err.response.status_code == 404:
            print('Ошибка в номере запуска')
        else:
            print(f'Возникла ошибка: {err}')


if __name__ == '__main__':
    main()
