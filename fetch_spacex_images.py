import argparse
import requests
from utils import save_image
from pathlib import Path

def fetch_spacex_images(launch_id=None):
    if launch_id:
        spacex_api_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    else:
        spacex_api_url = "https://api.spacexdata.com/v5/launches/latest"

    response = requests.get(spacex_api_url)
    response.raise_for_status()
    launch_data = response.json()

    image_urls = launch_data["links"]["flickr"]["original"]

    if not image_urls:
        print("Нет изображений для этого запуска.")
        return

    output_folder = Path("images/spacex")
    output_folder.mkdir(parents=True, exist_ok=True)

    for index, image_url in enumerate(image_urls):
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        filename = f"spacex_{index + 1}.jpg"
        save_image(image_response.content, output_folder, filename)

if name == "__main__":
    parser = argparse.ArgumentParser(description="Скачать изображения SpaceX по ID запуска")
    parser.add_argument("--launch_id", help="ID запуска SpaceX")
    args = parser.parse_args()

    fetch_spacex_images(args.launch_id)
