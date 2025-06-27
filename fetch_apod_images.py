import requests
from utils import setup_env, get_image_extension, save_image


def fetch_apod_images(image_count=30):
    api_key, download_folder = setup_env()

    api_url = "https://api.nasa.gov/planetary/apod"
    query_params = {
        "count": image_count,
        "api_key": api_key
    }

    response = requests.get(api_url, params=query_params)
    response.raise_for_status()
    apod_entries = response.json()

    for index, apod_entry in enumerate(apod_entries, start=1):
        if apod_entry.get("media_type") != "image":
            continue

        image_url = apod_entry["url"]
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        file_extension = get_image_extension(image_url)
        filename = f"nasa_apod_{index}{file_extension}"

        save_image(image_response.content, download_folder, filename)


if __name__ == "__main__":
    fetch_apod_images()
