# Игра: Сапёр
#
# Цель игры: открыть все клетки, не содержащие мин.
#
# Правила игры:
#
# 1. Игровое поле состоит из клеток размером 5x5.
# 2. На поле случайным образом размещены 5 мин.
# 3. Игрок вводит координаты клетки (например, "2 3" для второй строки и третьего столбца), чтобы проверить ее.
# 4. Если игрок открывает клетку с миной, он проигрывает.
# 5. Если игрок открывает клетку без мины, на этой клетке отображается число, указывающее, сколько мин находится в соседних клетках (по горизонтали, вертикали и диагоналям).
# 6. Игрок побеждает, если открывает все клетки, не содержащие мин.
#
# Пример игрового процесса:
#
# 1. Игроку показывается пустое поле:
# - - - - -
# - - - - -
# - - - - -
# - - - - -
# - - - - -
#
# 2. Игрок вводит координаты клетки:
# Введите координаты клетки (строка столбец): 2 3
#
# 3. Если в этой клетке нет мины, открывается число:
# - - - - -
# - - 1 - -
# - - - - -
# - - - - -
# - - - - -
#
# 4. Игрок продолжает вводить координаты, пока не откроет все безопасные клетки или не попадет на мину.
# 5. Если игрок открывает клетку с миной, игра заканчивается:
# - - - - -
# - - * - -
# - - - - -
# - - - - -
# - - - - -
# Вы проиграли! Вы попали на мину.
#
# 6. Если игрок открывает все клетки без мин, игра заканчивается победой:
# - 1 1 1 -
# - 1 * 1 -
# - 2 2 2 -
# - 1 * 1 -
# - 1 1 1 -
# Поздравляем! Вы открыли все безопасные клетки.
import random

def mine_sweeper():
    field = [[0 for i in range(5)] for a in range(5)]
    n = 0
    while True:
        if n == 5:
            break
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if field[y][x] == 0:
            field[y][x] = 1
            n+=1
    # print(field)

    field_pl = [['-' for i in range(5)] for a in range(5)]
    n = 0
    while True:
        for y in range(5):
            print()
            for x in range(5):
                print(field_pl[y][x], end=' ')
        print()
        if n == 20:
            print('Вы победили!!!!!')
            break
        x = input('Координата x: ')
        y = input('Координата y: ')
        if x == 'x' or y == 'x':
            break
        if field[int(y) - 1][int(x) - 1] == 1:

            for y in range(5):
                for x in range(5):
                    if field[y][x] == 1:
                        field_pl[y][x] = '*'
            for y in range(5):
                print()
                for x in range(5):
                    print(field_pl[y][x], end=' ')
            print()
            print('ВЫ ПРОИГРАЛИ')
            break
        else:
            sum_mine = 0
            if int(y) == 1:
                y1 = 0
                y2 = 1
            elif int(y) == 5:
                y1 = 3
                y2 = 4
            else:
                y1 = int(y)-2
                y2 = int(y)
            if int(x) == 1:
                x1 = 0
                x2 = 1
            elif int(x) == 5:
                x1 = 3
                x2 = 4
            else:
                x1 = int(x) -2
                x2 = int(x)
            for a in range(y1, y2+1):
                for b in range(x1, x2+1):
                    if field[a][b]==1:
                        sum_mine +=1
            field_pl[int(y)-1][int(x)-1]= sum_mine
            n += 1






if __name__ == '__main__':
    mine_sweeper()