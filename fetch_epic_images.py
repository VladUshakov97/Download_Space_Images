
import requests
import os
from datetime import datetime, timedelta
from utils import setup_env, save_image

def fetch_epic_images(days_to_fetch=2, max_photos_per_day=5):
    api_key, base_folder = setup_env()
    epic_folder = os.path.join(base_folder, "epic")

    start_date = datetime.today() - timedelta(days=1)

    for day_offset in range(days_to_fetch):
        target_date = start_date - timedelta(days=day_offset)
        date_str = target_date.strftime("%Y-%m-%d")

        api_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}"
        query_params = {"api_key": api_key}

        response = requests.get(api_url, params=query_params)
        response.raise_for_status()
        epic_images = response.json()

        if not epic_images:
            print(f"Нет фото за {date_str}")
            continue

        print(f"Найдено {len(epic_images)} фото за {date_str}")

        for entry in epic_images[:max_photos_per_day]:
            image_name = entry["image"]
            year, month, day = date_str.split("-")

            image_url = (
                f"https://epic.gsfc.nasa.gov/archive/natural/"
                f"{year}/{month}/{day}/png/{image_name}.png"
            )

            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                save_image(image_response.content, epic_folder, f"{image_name}.png")
            except requests.HTTPError as error:
                print(f"Ошибка при скачивании {image_name}: {error}")

if __name__ == "__main__":
    fetch_epic_images()
