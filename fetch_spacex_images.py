import argparse
import requests
from utils import save_image
from pathlib import Path

def fetch_spacex_images(launch_id=None):
    if launch_id:
        url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    else:
        url = "https://api.spacexdata.com/v5/launches/latest"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    images = data["links"]["flickr"]["original"]

    if not images:
        print("Нет изображений для этого запуска.")
        return

    folder = Path("images/spacex")
    for index, img_url in enumerate(images):
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        filename = f"spacex_{index+1}.jpg"
        save_image(img_response.content, folder, filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачать изображения SpaceX по ID запуска")
    parser.add_argument("--launch_id", help="ID запуска SpaceX")
    args = parser.parse_args()
    fetch_spacex_images(args.launch_id)
