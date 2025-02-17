import os
import argparse
from pathlib import Path
from telegram.error import TelegramError
from dotenv import load_dotenv
from post_image_tg import post_image


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()
    
    file_name = Path(args.file_name)
    if not file_name.is_file():
        print('Неверное имя файла')
        return

    chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TG_TOKEN']
    try:
        post_image(file_name=file_name, chat_id=chat_id, token=token)
    except TelegramError as err:
        print(f'Не удалось опубликовать картинку {file_name}. Ошибка: {err.message}')
    

if __name__ == '__main__':
    main()
