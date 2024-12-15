import requests


def download_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Проверка на ошибки
    return response.text
