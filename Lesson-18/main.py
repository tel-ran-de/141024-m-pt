import guess_number
import  minesweeper
import rock_paper_scissors
import quiz_game
import hangman
import text_adventure


while True:
    print()
    print('------Выберете игру:-------')
    print('1. Угадай число')
    print('2. Камень, ножницы, бумага')
    print('3. Викторина')
    print('4. Виселица')
    print('5. Текстовый квест')
    print('6. Сапер')
    print('7. Выход')
    choise = input('Ваш выбор: ')
    if choise == '7':
        print('До новых встреч!')
        break

    if choise == '1':
        guess_number.gu_nu()

    if choise == '2':
        rock_paper_scissors.r_p_s()

    if choise == '3':
        quiz_game.qu_ga()

    if choise == '4':
        hangman.ha_ma()

    if choise == '5':
        text_adventure.tex_ad()

    if choise == '6':
        minesweeper.mine_sweeper()
    #