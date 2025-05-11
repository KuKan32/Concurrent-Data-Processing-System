import concurrent.futures
from downloader import download_url
from processor import process_data


def main():
    # Чтение URL из файла
    with open('urls.txt', 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    # Использование ThreadPoolExecutor для параллельной загрузки
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(download_url, url): url for url in urls}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                processed_data = process_data(data)
                print(f"Processed data from {url}: {processed_data}")
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")


if __name__ == "__main__":
    main()
