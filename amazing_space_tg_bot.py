import os
import argparse
import telegram
import time
import random
from dotenv import load_dotenv


def post_image(file_name):
    file_size = os.path.getsize(file_name)
    if file_size > 20 * 10 ** 6:
        return

    token = os.environ['TG_TOKEN']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=token)
    try:
        bot.send_photo(chat_id=chat_id, photo=open(file_name, 'rb'))
    except Exception:
        return


def main():
    load_dotenv()
    images_dir = './images'

    parser = argparse.ArgumentParser()
    parser.add_argument('posting_frequency', nargs='?')
    args = parser.parse_args()
    if args.posting_frequency:
        posting_frequency = args.posting_frequency
    else:
        posting_frequency = os.environ['POSTING_FREQUENCY']

    # TODO удалить
    posting_frequency = 2 / 60 / 60
    
    file_names = []
    for root, _, files in os.walk(images_dir):
        for file in files:
            file_names.append(os.path.join(root, file))
    
    while True:
        for file_name in file_names:
            post_image(file_name)
            time.sleep(posting_frequency * 60 * 60)
        random.shuffle(file_names)


if __name__ == '__main__':
    main()
