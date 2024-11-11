from random import randint
def gu_nu():
    a = randint(1,100)
    n = []
    while True:
        print('-----------')
        if len(n) == 6:
            print(f'У тебя нет больше попыток ты проиграл!!\nЗагаданное число было {a}')
            print(f'Ваши числа {n}')
            break
        choise = int(input(f'у тебя {6-len(n)} попыток\nпопробуй угадай: '))
        n.append(choise)
        if choise == a:
            print(f'Вы угадали число {a}, с {len(n)} попытки!!!!')
            print(f'Ваши числа {n}')
            break
        elif choise <= a:
            print('Не угадал, загаданное число больше')
        else:
            print('Не угадал, загаданное число меньше')


if __name__ == '__main__':
    gu_nu()