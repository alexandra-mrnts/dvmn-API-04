import os
import telegram


TG_FILE_MAX_SIZE = 20


def is_file_size_ok(filepath, max_size):
    file_size = os.path.getsize(filepath)
    return file_size <= max_size * 10 ** 6


def post_image(filepath, chat_id, token):
    if not is_file_size_ok(filepath, TG_FILE_MAX_SIZE):
        return
    bot = telegram.Bot(token=token)
    with open(filepath, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)
