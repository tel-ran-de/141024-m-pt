# Тема: Сторонние модули

# Задание: Установка Django в виртуальную среду
#
# 1. Установка виртуального окружения
# Создайте отдельную папку для выполнения задания. Перейдите в эту папку в терминале (команда cd <название папки>)
# Для создания виртуальной среды используйте модуль `venv`, который встроен в Python 3.
# myenv - имя для папки с виртуальной средой
# Находясь в папке задания в терминале введите python -m venv myenv
#
# 2. Активация виртуальной среды
# После создания виртуального окружения, его нужно активировать.
# На Windows (git bash): source myenv/Scripts/activate
# На Windows (cmd или PowerShell): myenv\Scripts\activate
# На MacOS и Linux: source myenv/bin/activate
#
# 3. Установка Django
# Когда виртуальная среда активирована, можно установить Django с помощью `pip`.
# pip install django
# python -m pip install django
#
# 4. Проверка установки Django
# После установки Django проверьте его версию, чтобы убедиться, что установка прошла успешно.
# django-admin --version
# pip freeze
#
# 5. Создайте файл requirements.txt, где будет указан django.
# pip freeze > requirements.txt - создаст файл со списком библиотек нужных проекты
#
#  pip install -r requirements.txt - установит все библиотеки с указанными версиями из файла requirements.txt
# После завершения работы в виртуальной среде, её можно деактивировать: deactivate

# pip freeze