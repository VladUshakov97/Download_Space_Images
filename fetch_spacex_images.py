import argparse
import requests
from utils import save_image
from pathlib import Path

def fetch_spacex_images(launch_id="latest"):
    api_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"

    response = requests.get(api_url)
    response.raise_for_status()
    spacex_launch = response.json() 

    image_urls = spacex_launch["links"]["flickr"]["original"]

    if not image_urls:
        print("Нет изображений для этого запуска.")
        return

    output_folder = Path("images/spacex")
    output_folder.mkdir(parents=True, exist_ok=True)

    for index, image_url in enumerate(image_urls, start=1):
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        filename = f"spacex_{index}.jpg"
        save_image(image_response.content, output_folder, filename)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Скачать изображения SpaceX по ID запуска (по умолчанию — последний)")
    parser.add_argument(
        "--launch_id",
        default="latest",
        help="ID запуска SpaceX (по умолчанию: 'latest')"
    )
    args = parser.parse_args()

    fetch_spacex_images(args.launch_id)
