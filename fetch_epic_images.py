import requests
import os
from datetime import datetime, timedelta
from utils import setup_env, save_image

def fetch_epic_images(days_to_fetch=2, photos_per_day=5):
    api_key, folder = setup_env()
    folder = os.path.join(folder, "epic")
    start_date = datetime.today() - timedelta(days=1)

    for day_offset in range(days_to_fetch):
        date = start_date - timedelta(days=day_offset)
        date_str = date.strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}"
        params = {"api key": api key}
        response = requests.get(url, params=params)
        data = response.json()

        if not data:
            print(f"Нет фото за {date_str}")
            continue

        print(f"Найдено {len(data)} фото за {date_str}")

        for item in data[:photos_per_day]:
            image_name = item["image"]
            parts = date_str.split("-")
            image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{parts[0]}/{parts[1]}/{parts[2]}/png/{image_name}.png"
            img_response = requests.get(image_url)
            if img_response.status_code == 200:
                save_image(img_response.content, folder, f"{image_name}.png")
            else:
                print(f"Ошибка при скачивании {image_name}")

if __name__ == "__main__":
    fetch_epic_images()
