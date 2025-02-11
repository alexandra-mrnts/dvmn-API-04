import os
import argparse
import time
import random
from dotenv import load_dotenv
from post_image_tg import post_image


def main():
    load_dotenv()
    images_dir = './images'

    parser = argparse.ArgumentParser()
    parser.add_argument('posting_frequency', nargs='?')
    args = parser.parse_args()
    if args.posting_frequency:
        posting_frequency = args.posting_frequency
    else:
        posting_frequency = int(os.environ['POSTING_FREQUENCY'])

    file_names = []
    for root, _, files in os.walk(images_dir):
        for file in files:
            file_names.append(os.path.join(root, file))
    
    chat_id = os.environ['CHAT_ID']
    token = os.environ['TG_TOKEN']
    while True:
        for file_name in file_names:
            post_image(file_name=file_name, chat_id=chat_id, token=token)
            time.sleep(posting_frequency * 60 * 60)
        random.shuffle(file_names)


if __name__ == '__main__':
    main()
