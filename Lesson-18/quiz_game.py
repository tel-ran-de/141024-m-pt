# Игра: Викторина
#
# Создайте игру "Викторина", где пользователю задаются 5 вопросов с вариантами ответов.
# После выбора варианта ответ выводится, правильный ли был сделан выбор.
# В конце игры выводится общее количество правильных ответов.
#
# Столица Франции?
# — 1. Лондон
# — 2. Берлин
# — 3. Париж
#
# Столица Германии?
# — 1. Лондон
# — 2. Берлин
# — 3. Венеция
#
# Столица США?
# — 1. Нью-Йорк
# — 2. Лос-Анджелес
# — 3. Вашингтон
#
# Столица Греции
# — 1. Афины
# — 2. Стамбул
# — 3. Киев
#
# Столица Норвегии
# — 1. Осло
# — 2. Порту
# — 3. Мюнхен
import random
from random import randint


def qu_ga():
    dict_capitals = {"Франции":"Париж", "Германии":"Берлин", "США":"Вашингтон", "Греции":"Афины",
                     "Норвегии":"Осло"}


    city =["Осло", "Порту", "Мюнхен", "Киев", "Стамбул", "Афины", "Вашингтон",
               "Лос-Анджелес", "Нью-Йорк", "Венеция", "Берлин",
               "Лондон", "Париж"]
    # print(city)
    lands =[]
    lands_ans = []
    capitals_ans =[]


    for i in dict_capitals: # создан список всех стран
        lands.append(i)

    random.shuffle(lands)
    lands_ans = lands[:5] # создан список из 5 рандомных стран


    quiz_sum = 0
    while len(lands_ans) > 0:

        print()
        print()
        print('--------------')
        print(f'Столица {lands_ans[-1]}')
        capitals_ans.clear()
        capitals_ans.append(dict_capitals[lands_ans[-1]])
        while len(capitals_ans) < 3:
            a = random.choice(city)
            if not a in capitals_ans:
                capitals_ans.append(a)  # список на выбор из 3 городов

        random.shuffle(capitals_ans)

        while True:

            print('--------------')
            for n in range(1,4):
                print(f'{n}. {capitals_ans[n-1]}')
            print()
            ans = input('Твой ответ: ')
            if ans == '1' or ans == '2' or ans == '3':
                if dict_capitals[lands_ans[-1]] == capitals_ans[int(ans) - 1]:
                    print()
                    print(f'Совершенно верно столица {lands_ans[-1]} это {dict_capitals[lands_ans[-1]]}')
                    quiz_sum += 1
                    break
                else:
                    print(f'Не угадал на самом деле столица {lands_ans[-1]} это {dict_capitals[lands_ans[-1]]}')
                    break
            else:
                print('Неверный ввод')

        lands_ans = lands_ans[:-1]
        if len(lands_ans) == 0:
            print(f'Правильных ответов {quiz_sum}')


if __name__ == '__main__':
    qu_ga()