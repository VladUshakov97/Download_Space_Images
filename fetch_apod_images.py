import requests
from utils import setup_env, get_image_extension, save_image

def fetch_apod_images(count=30):
    api_key, folder = setup_env()
    url = f"https://api.nasa.gov/planetary/apod"
    params = {
        "count": count,
        "api key": api key
    }
    
    response = requests.get(url)
    response.raise_for_status()
    apod_items = response.json()

    for index, item in enumerate(apod_items):
        if item.get("media_type") != "image":
            continue
        img_url = item["url"]
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        ext = get_image_extension(img_url)
        filename = f"nasa_apod_{index + 1}{ext}"
        save_image(img_response.content, folder, filename)

if __name__ == "__main__":
    fetch_apod_images()
