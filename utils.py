import os
from pathlib import Path
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv

def get_image_extension(url):
    path = urlsplit(url).path
    path = unquote(path)
    return Path(path).suffix

def save_image(content, folder, filename):
    folder_path = Path(folder)
    folder_path.mkdir(parents=True, exist_ok=True)
    filepath = folder_path / filename
    with open(filepath, "wb") as f:
        f.write(content)
    print(f"Сохранено изображение: {filepath}")

def main():
    load_dotenv()  # Загрузка .env происходит здесь!
    nasa_api_key = os.getenv("NASA_API_KEY")
    save_path = os.getenv("PATH_TO_IMAGE", "images")
    
    # Пример вызова
    print(f"API Key: {nasa_api_key}, save path: {save_path}")

if __name__ == "__main__":
    main()
