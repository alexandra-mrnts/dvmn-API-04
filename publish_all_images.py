import os
import configargparse
import time
import random
from pathlib import Path
from telegram.error import TelegramError, Unauthorized
from dotenv import load_dotenv
from post_image_tg import post_image, is_file_size_ok, TG_FILE_MAX_SIZE


DEFAULT_IMAGE_DIR = 'images'
DEFAULT_POSTING_FREQUENCY = 4


def get_filepaths_from_dir(directory):
    filepaths = []
    for dirpath, _, filenames in directory.walk():
        for filename in filenames:
            filepaths.append(dirpath.joinpath(filename))
    return filepaths


def main():
    load_dotenv()

    parser = configargparse.ArgParser()
    parser.add_argument('-f',
                        '--frequency',
                        type=int,
                        env_var='TG_POSTING_FREQUENCY',
                        default=DEFAULT_POSTING_FREQUENCY)
    parser.add_argument('-d',
                        '--directory',
                        env_var='TG_IMAGE_SOURCE_DIR',
                        default=DEFAULT_IMAGE_DIR)
    args = parser.parse_args()

    source_dir = Path(args.directory).resolve()
    filepaths = get_filepaths_from_dir(source_dir)
    for filepath in filepaths:
        if not is_file_size_ok(filepath, TG_FILE_MAX_SIZE):
            filepaths.remove(filepath)
            print(f'Картинка {filepath} не может быть опубликована. Размер не должен превышать 20 Мб.')
    
    posting_frequency = args.frequency
    chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TG_TOKEN']
    err_count = 0
    while True:
        for filepath in filepaths:
            try:
                post_image(filepath=filepath, chat_id=chat_id, token=token)
            except Unauthorized:
                print('Ошибка. Неверный токен.')
                return
            except TelegramError as err:
                err_count += 1
                print(f'Не удалось опубликовать картинку {filepath}. Ошибка: {err.message}')
                if err_count >= 5:
                    print('Следующая попытка публикации через 5 минут.')
                    time.sleep(300)
                continue
            err_count = 0
            time.sleep(posting_frequency * 60 * 60)
        random.shuffle(filepaths)


if __name__ == '__main__':
    main()
