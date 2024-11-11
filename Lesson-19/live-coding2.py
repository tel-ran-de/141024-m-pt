# read
print('# read')
with open('text_files/example.txt', 'r') as file:
    content = file.read(5)
    print(content)  # Hello
    content = file.read(5)
    print(content)  # , Wor

    print(file.tell())  # 10
    file.seek(0)
    print(file.tell())  # 0
    content = file.read(5)
    print(content)  # Hello

# readline
print()
print('# readline')
with open('text_files/data.txt', 'r') as file:
    content = file.readline()
    print(content)  # Hello, World!
    print(file.tell())  # 15
    content = file.readline()
    print(content)  # This is a sample file.
    print(file.tell())  # 39

# readlines
print()
print('# readlines')
with open('text_files/data.txt', 'r') as file:
    content = file.readlines()
    print(content)  # ['Hello, World!\n', 'This is a sample file.\n', 'It contains multiple lines of text.\n', 'Each line is separated by a newline character.\n']
    print(file.tell())  # 124


# write в режиме 'w' очищает содержимое файла
print()
print("# write в режиме 'w' очищает содержимое файла")
with open('text_files/example.txt', 'w') as file:
    file.write('Hello, World!\n')

# write в режиме 'a' не очищает содержимое файла
print()
print("# write в режиме 'a' не очищает содержимое файла")
with open('text_files/example.txt', 'a') as file:
    file.write('Welcome to file handling in Python.')

# writelines
print()
print("# writelines")
with open('text_files/writelines.txt', 'w') as file:
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)
    # переместим курсор в начало файла
    file.seek(0)
    lines = ['Line -2\n', 'Line -1\n', 'Line 0\n']
    file.writelines(lines)
