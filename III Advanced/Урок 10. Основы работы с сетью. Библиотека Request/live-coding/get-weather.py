import requests
from pprint import pprint


def main():
    url = 'http://api.weatherapi.com/v1/current.json'

    key = '7d6b5bb050f74b1794c104006240212'

    params = {
        'key': key,
        'q':  'London',
        # 'aqi': 'no',
        # 'alerts': 'no'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)
    pprint(response.json())


if __name__ == '__main__':
    main()
