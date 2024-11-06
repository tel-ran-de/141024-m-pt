def greet(name):
    return f"Hello, {name}!"


print('Этот print срабатывает и при импорте модуля и при запуске скрипта.')


if __name__ == '__main__':
    print('Этот print срабатывает только при запуске скрипта.')