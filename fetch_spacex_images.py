import requests
import argparse
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from load_web_image import load_image


FILE_DIR = './images'


def fetch_spacex_launch_images(launch_id=None):
    url_template = 'https://api.spacexdata.com/v5/launches/'
    if launch_id:
        url = f'{url_template}{launch_id}'
    else:
        url = f'{url_template}latest'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as err:
        if response.status_code == 404:
            print('Ошибка в номере запуска')
        else:
            print(f'Возникла ошибка: {err}')
        return

    response_body = response.json()
    images = response_body['links']['flickr']['original']
    for image_number, image in enumerate(images):
        file_name = f'{FILE_DIR}/spacex_{str(image_number + 1)}.jpg'
        load_image(url=image, file_name=file_name)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', nargs='?')
    args = parser.parse_args()
    fetch_spacex_launch_images(args.launch_id)


if __name__ == '__main__':
    main()
