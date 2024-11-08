# открытие файла в бинарном режиме
file = open("backiee-198990-landscape.jpg", "rb")
contains = file.read()
print(contains)
file.close()