import os
import telegram


def post_image(file_name, chat_id, token):
    file_size = os.path.getsize(file_name)
    if file_size > 20 * 10 ** 6:
        return
    bot = telegram.Bot(token=token)
    try:
        bot.send_photo(chat_id=chat_id, photo=open(file_name, 'rb'))
    except Exception:
        return
