# Загрузка изображений из космоса
Скрипты для загрузки изображений с открытых API NASA (APOD, EPIC) и SpaceX.
## Переменные окружения
Программа использует переменные окружения, которые необходимо указать в файле '.env' в корневой директории проекта. 
- NASA_API_KEY — API-ключ для получения изображений NASA. Можно получить на сайте [api.nasa.gov](https://api.nasa.gov).
- PATH_TO_IMAGE — путь к папке для сохранения изображений с NASA. По умолчанию используется "images".

- TELEGRAM_BOT_TOKEN — токен Telegram-бота. Получается у [BotFather](https://t.me/BotFather).
- TELEGRAM_CHAT_ID — ID чата, в который будут отправляться изображения.
- PUBLISH_DELAY — задержка между публикациями изображений в Telegram (в часах). По умолчанию — 4 часа.

Пример содержимого .env:

```env
NASA_API_KEY=DEMO_KEY
PATH_TO_IMAGE=images
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=123456789
PUBLISH_DELAY=4
```
### Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/VladUshakov97/Download_Space_Images
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Создайте .env файл с вашим NASA API ключом:
```env
NASA_API_KEY=ваш_ключ_от_nasa_api
```
## Использование
### APOD (Astronomy Picture of the Day)
```bash
python fetch_apod_images.py
```
### EPIC (Earth Polychromatic Imaging Camera)
```bash
python fetch_epic_images.py
```
### SpaceX
Скачать изображения последнего запуска:
```bash
python fetch_spacex_images.py
```
Или скачать по конкретному launch_id:
```bash
python fetch_spacex_images.py --launch_id <ID_запуска>
```
### Файл utils.py
Содержит вспомогательные функции:
* setup_env() - загрузка переменных окружения и создание папок.
* get_image_extension(url) - получение расширения файла из URL.
* save_image(content, folder, filename) - сохранения изображния в файл.

# Автоматическая публикация фотографий в Telegram
## Скрипт publish_photos.py
Этот скрипт автомотичеси публекует изображения из указанной директории в Telegram-канал с заданной переодичностью.
### Как использовать 
1. Установите зависимости:
```bash
pip install -r requirements.txt
```
2. Создайте файл .env в корне проекта и добавьте туда ваш токен и ID/название канала:
```
TELEGRAM_BOT_TOKEN=ваш_токен_бота
TELEGRAM_CHAT_ID=@ваш_канал
```
3. Запустите скрипт:
```bash
python publish_photos.py --dir "ваш путь до папки с изображениями" --delay '4'
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).


