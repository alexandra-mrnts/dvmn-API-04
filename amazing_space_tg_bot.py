import os
import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id='@cosmophoto777', text='Добро пожаловать в космос!')
