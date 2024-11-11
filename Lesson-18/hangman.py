# Игра "Виселица"
#
# Напишите программу для игры "Виселица". Игроку дается слово, которое он должен угадать, называя буквы.
# Если игрок называет неправильную букву, ему начисляется штрафное очко.
# Игра заканчивается победой при угадывании слова или проигрышем при достижении лимита штрафных очков.
#
# Требования:
#
# 1. Программа должна случайным образом выбирать слово из списка.
# 2. Игрок должен иметь возможность вводить буквы по одной за попытку.
# 3. Если игрок угадал букву, она должна отображаться в правильных позициях в слове.
# Вместо остальных (скрытых) букв показываются звездочки *.
# 4. Если игрок назвал неправильную букву, количество штрафных очков должно увеличиваться.
# 5. Игра заканчивается победой, если все буквы слова угаданы, или проигрышем,
# если количество штрафных очков достигает лимита (например, 6).
from optparse import Option
# ______
#  |  |
#  |  O
#  | /|\
#  | / \

import random

def ha_ma():
    # список слов
    li_ha_ma = ["ПОЗИЦИЯ", "РОЛЬ", "СКОРОХОД", "МЫЛО", "РОК"]
    # функция прорисовки

    foul_ha_ma = 0
    def f_bild(foul_ha_ma):
        if foul_ha_ma == 0:
            print()
            print()
            print()
            print()
            print()
        elif foul_ha_ma ==1:
            print()
            print(' |')
            print(' |')
            print(' |')
            print(' |')
        elif foul_ha_ma == 2:
            print('_________')
            print(' |')
            print(' |')
            print(' |')
            print(' |')
        elif foul_ha_ma == 3:
            print('_________')
            print(' |')
            print(' |')
            print(' |')
            print(" |  / \\")
        elif foul_ha_ma == 4:
            print('_________')
            print(' |')
            print(' |')
            print(' |   |')
            print(' |  / \\')
        elif foul_ha_ma == 5:
            print('_________')
            print(' | ')
            print(' | ')
            print(' |  /|\\')
            print(' |  / \\')
        elif foul_ha_ma == 6:
            print('_________')
            print(' |   | ')
            print(' |   O ')
            print(' |  /|\\')
            print(' |  / \\')


    # рандом слова для угадывания

    word = random.choice(li_ha_ma)
    # print(word)
    word_menu = ["*" for i in word]
    # print(word_menu)
    abc_ha_ma =[]
    while True:
        f_bild(foul_ha_ma)
        for i in word_menu:
            print(i, sep=' ', end='')
        print()
        p_letter = input("Буква ")
        if p_letter.upper() in abc_ha_ma:
            print('Вы загадывали такую букву')
            # foul_ha_ma += 1
        elif p_letter.upper() in word and not p_letter.upper() in abc_ha_ma:
            for i in range(len(word)):
                if word[i] == p_letter.upper():
                    word_menu[i] = p_letter.upper()
        else:
            print('В этом слове нет такой буквы')
            foul_ha_ma += 1
        if not '*' in word_menu:
            print('Слово найдено, до новых встреч')
            break
        if foul_ha_ma == 6:
            f_bild(foul_ha_ma)
            print(f'Лууузеееееееррррр!!!!!\nзагаданное слово - {word}')
            break



if __name__ == '__main__':
    ha_ma()