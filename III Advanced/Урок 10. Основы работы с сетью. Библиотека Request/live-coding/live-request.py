import requests
import time


def search_request(search_query):
    # URL для поиска в Google
    url = "https://www.google.com/search"

    # Параметры запроса
    params = {
        'q': search_query,
        # 'hl': 'en',  # Язык интерфейса
        # 'lr': 'lang_en',  # Язык результатов
        # 'gl': 'us'  # Регион (например, 'us' для США)
    }

    # Заголовки, чтобы имитировать браузер
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Выполнение GET-запроса
    response = requests.get(url, params=params, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Печать URL запроса
        print(f"Requested URL: {response.url}")
        # Печать содержимого ответа
        print(response.text[:1000])
    elif response.status_code == 429:
        print(f"Rate limit exceeded. Retrying after {response.headers.get('Retry-After')} seconds.")
        retry_after = int(response.headers.get('Retry-After', 60))
        time.sleep(retry_after)
        search_request(search_query)  # Retry the request
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")


def main():
    search_request('python')


if __name__ == '__main__':
    main()
