import os
import time
import argparse
import random
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")       


def send_photo(photo_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': CHAT_ID, 'caption': f"Фото из космоса"}
        response = requests.post(url, files=files, data=data)
        print(f"Отправлено {photo_path}: {response.status_code}")
        if not response.ok:
            print(response.text)


def publish_photos(directory, delay_hours):
    delay_seconds = delay_hours * 3600
    all_photos = [os.path.join(directory, f) for f in os.listdir(directory)
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    while True:
        random.shuffle(all_photos)
        for photo_path in all_photos:
            send_photo(photo_path)
            time.sleep(delay_seconds)


def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    parser = argparse.ArgumentParser(description="Публикует фото в Telegram с заданной задержкой.")
    parser.add_argument('--dir', default='images', help='Путь к директории с фотографиями')
    parser.add_argument('--delay', type=float, default=float(os.getenv('PUBLISH_DELAY', 4)),
                        help='Задержка между публикациями (в часах)')
    args = parser.parse_args()

    if not BOT_TOKEN or not CHAT_ID:
        print("Ошибка: TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID должны быть заданы в .env")
        return

    publish_photos(args.dir, args.delay)


if __name__ == "__main__":
    main()
