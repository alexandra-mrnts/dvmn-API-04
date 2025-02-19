import os
import argparse
from pathlib import Path
from telegram.error import TelegramError, Unauthorized
from dotenv import load_dotenv
from post_image_tg import post_image


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    
    filepath = Path(args.filename)
    if not filepath.is_file():
        print('Неверное имя файла')
        return

    chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TG_TOKEN']
    try:
        post_image(filepath=filepath, chat_id=chat_id, token=token)
    except Unauthorized:
        print('Ошибка. Неверный токен.')
    except TelegramError as err:
        print(f'Не удалось опубликовать картинку {filepath}. Ошибка: {err.message}')
    

if __name__ == '__main__':
    main()
