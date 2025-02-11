import os
import requests
import datetime
from dotenv import load_dotenv
from load_web_image import load_image


FILE_DIR = './images'
DEFAULT_MAX_PICS_NUMBER = 5


def fetch_NASA_EPIC_images():
    url = 'https://api.nasa.gov/EPIC/api/natural'
    api_key = os.environ['NASA_API_KEY']
    params = {'api_key': api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_body = response.json()

    try:
        max_pics_number = int(os.environ['NASA_EPIC_PICS_NUMBER'])
    except KeyError:
        max_pics_number = DEFAULT_MAX_PICS_NUMBER

    for image_number, image in enumerate(response_body):
        if image_number >= (max_pics_number):
            return
        image_name = image['image']
        image_date = datetime.datetime.fromisoformat(image['date'])
        image_date = image_date.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={api_key}'
        file_name = f'{FILE_DIR}/EPIC_{str(image_number + 1)}.png'
        load_image(url=image_url, file_name=file_name)


def main():
    load_dotenv()
    fetch_NASA_EPIC_images()


if __name__ == '__main__':
    main()
