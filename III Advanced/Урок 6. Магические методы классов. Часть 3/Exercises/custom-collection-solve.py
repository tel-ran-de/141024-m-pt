# Создайте класс CustomCollection, который будет поддерживать методы __getitem__, __setitem__ и __delitem__.

import time
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CustomCollection:
    def __init__(self):
        self.data = {}
        self.ttl = {}

    def __getitem__(self, key):
        logging.info(f"Getting the value for key: {key}")
        if key in self.ttl and time.time() > self.ttl[key]:
            del self.data[key]
            del self.ttl[key]
            raise KeyError(f"Key {key} has expired")
        return self.data[key]

    def __setitem__(self, key, value, ttl=None):
        logging.info(f"Setting the value for key: {key} to {value}")
        self.data[key] = value
        if ttl:
            self.ttl[key] = time.time() + ttl

    def __delitem__(self, key):
        logging.info(f"Deleting the value for key: {key}")
        if key in self.data:
            del self.data[key]
        if key in self.ttl:
            del self.ttl[key]

    def __repr__(self):
        return repr(self.data)

    def set_multiple(self, **kwargs):
        logging.info(f"Setting multiple values: {kwargs}")
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def get_multiple(self, *keys):
        logging.info(f"Getting multiple values for keys: {keys}")
        return {key: self.__getitem__(key) for key in keys if key in self.data}

    def delete_multiple(self, *keys):
        logging.info(f"Deleting multiple values for keys: {keys}")
        for key in keys:
            if key in self.data:
                self.__delitem__(key)

    def sorted_items(self):
        logging.info("Getting sorted items")
        return dict(sorted(self.data.items()))


def main():
    # Тестирование
    cc = CustomCollection()
    cc['x'] = 100  # Setting the value for key: x to 100
    cc['y'] = 200  # Setting the value for key: y to 200
    cc.set_multiple(a=300, b=400)  # Setting multiple values

    print(cc['x'])  # Getting the value for key: x, Output: 100
    print(cc)  # Output: {'x': 100, 'y': 200, 'a': 300, 'b': 400}

    print(cc.get_multiple('x', 'y', 'z'))  # Getting multiple values for keys: x, y, z, Output: {'x': 100, 'y': 200}

    cc.delete_multiple('x', 'y')  # Deleting multiple values for keys: x, y
    print(cc)  # Output: {'a': 300, 'b': 400}

    cc['temp'] = 500, 5  # Setting the value for key: temp to 500 with TTL 5 seconds
    print(cc)
    time.sleep(8)
    try:
        print(cc['temp'])  # Should raise KeyError as the key has expired
    except KeyError as e:
        print(e)
    print(cc['temp'])
    print(cc.sorted_items())  # Getting sorted items, Output: {'a': 300, 'b': 400}


if __name__ == '__main__':
    main()
