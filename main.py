import os
import requests
import datetime
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlsplit


def filetype(url):
    path = urlsplit(url).path
    extension = os.path.splitext(path)[1]
    return extension


def load_picture(url, file_name):
    response = requests.get(url)
    response.raise_for_status()
    Path(file_name).parent.mkdir(exist_ok=True)
    with open(file_name, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(launch_id=None):
    file_dir = './images'
    url_template = 'https://api.spacexdata.com/v5/launches/'
    if launch_id:
        url = url_template + launch_id
    else:
        url = url_template + 'latest'

    response = requests.get(url)
    response_body = response.json()
    images = response_body['links']['flickr']['original']
    for image_number, image in enumerate(images):
        file_name = f'{file_dir}/spacex_{str(image_number + 1)}.jpg'
        load_picture(url=image, file_name=file_name)


def fetch_NASA_apod():
    supported_extentions = ('.jpg', '.jpeg', '.png', '.gif')
    pics_number = 5
    file_dir = './images'

    url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.environ['NASA_API_KEY']
    params = {'count': pics_number, 'api_key': api_key}
    response = requests.get(url=url, params=params)
    response_body = response.json()

    for item_number, item in enumerate(response_body):
        image = item['url']
        extention = filetype(image)
        if extention.lower() not in supported_extentions:
            continue
        file_name = f'{file_dir}/nasa_apod_{str(item_number + 1)}{extention}'
        load_picture(url=image, file_name=file_name)


def fetch_NASA_EPIC():
    max_pics_number = 5
    file_dir = './images'

    api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url=url, params=params)
    response_body = response.json()

    for item_number, item in enumerate(response_body):
        image_name = item['image']
        image_date = datetime.datetime.fromisoformat(item['date'])
        image_date = image_date.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={api_key}'
        file_name = file_dir + '/EPIC_' + str(item_number + 1) + '.png'
        load_picture(url=image_url, file_name=file_name)
        if item_number >= (max_pics_number - 1):
            break


def main():
    load_dotenv()
    fetch_spacex_launch('5eb87d47ffd86e000604b38a')
    # fetch_spacex_launch()
    fetch_NASA_apod()
    fetch_NASA_EPIC()


if __name__ == '__main__':
    main()
