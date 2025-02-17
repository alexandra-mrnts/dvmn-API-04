import os
import configargparse
import time
import random
from pathlib import Path
from telegram.error import TelegramError
from dotenv import load_dotenv
from post_image_tg import post_image


DEFAULT_IMAGE_DIR = 'images'
DEFAULT_POSTING_FREQUENCY = 4


def get_files_from_dir(dir):
    files = []
    for dirpath, _, file_names in dir.walk():
        for file_name in file_names:
            files.append(dirpath.joinpath(file_name))
    return files


def main():
    load_dotenv()

    parser = configargparse.ArgParser()
    parser.add_argument('-f',
                        '--frequency',
                        env_var='TG_POSTING_FREQUENCY',
                        default=DEFAULT_POSTING_FREQUENCY)
    parser.add_argument('-d',
                        '--directory',
                        env_var='TG_IMAGE_SOURCE_DIR',
                        default=DEFAULT_IMAGE_DIR)
    args = parser.parse_args()

    source_dir = Path(args.directory).resolve()
    posting_frequency = int(args.frequency)
    files = get_files_from_dir(source_dir)    
    chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TG_TOKEN']
    
    while True:
        for file in files:
            try:
                post_image(file_name=file, chat_id=chat_id, token=token)
            except TelegramError as err:
                print(f'Не удалось опубликовать картинку {file}. Ошибка: {err.message}')
                continue
            time.sleep(posting_frequency * 60 * 60)
        random.shuffle(files)


if __name__ == '__main__':
    main()
