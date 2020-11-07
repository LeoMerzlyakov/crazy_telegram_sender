import os
import time

from dotenv import load_dotenv

import telegram

load_dotenv()


CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

tg_bot = telegram.Bot(token=TELEGRAM_TOKEN)


def send_message(text_massge):
    return tg_bot.send_message(chat_id=CHAT_ID, text=text_massge)


def main():
    mesege_number = 1
    while True:
        try:
            text = f"Messege # {mesege_number}. + test autodeploy."
            send_message(text)
            time.sleep(300)
            mesege_number += 1

        except Exception as e:
            print(f'Бот упал с ошибкой: {e}')
            time.sleep(300)
            continue


if __name__ == '__main__':
    main()
