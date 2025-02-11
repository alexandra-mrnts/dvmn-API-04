import os
import argparse
from dotenv import load_dotenv
from post_image_tg import post_image


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()
    file_name = args.file_name
    chat_id = os.environ['CHAT_ID']
    token = os.environ['TG_TOKEN']
    post_image(file_name, chat_id, token)
            

if __name__ == '__main__':
    main()
