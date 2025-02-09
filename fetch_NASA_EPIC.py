import os
import requests
import datetime
from dotenv import load_dotenv
from load_web_image import load_image


def fetch_NASA_EPIC_images():
    max_pics_number = 5
    file_dir = './images'

    api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_body = response.json()

    for item_number, item in enumerate(response_body):
        image_name = item['image']
        image_date = datetime.datetime.fromisoformat(item['date'])
        image_date = image_date.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={api_key}'
        file_name = file_dir + '/EPIC_' + str(item_number + 1) + '.png'
        load_image(url=image_url, file_name=file_name)
        if item_number >= (max_pics_number - 1):
            break


def main():
    load_dotenv()
    fetch_NASA_EPIC_images()


if __name__ == '__main__':
    main()
