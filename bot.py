# bot.py
from telegram_handler import TelegramHandler

def main():
    telegram_handler = TelegramHandler()
    telegram_handler.start_bot()

if __name__ == "__main__":
    main()