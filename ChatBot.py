import random

def welcome_message():
    username = input("Введите ваше имя: ")
    print('Приятно познакомиться, ' + username + '!')
    print(username + ', давай сыграем в игру "Угадай масть". '
                     'Я загадаю игральную карту, а ты угадаешь ее масть! ')
    attempts = 3
    print(username + ', у тебя будет ' + str(attempts) + ' попытки')
    return username, attempts


def play_game(attempts):
    CARD_SUIT = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    CARD_NUMBERS = ['2', '3', '4', '5', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    red = ['Diamonds', 'Hearts']
    black = ['Spades', 'Clubs']

    while attempts > 0:
        user_suit_card = input('Введи масть загаданной мною карты:\n ').capitalize()
        if user_suit_card in ['Red', 'Black']:
            my_card = random.choice(list(zip(CARD_NUMBERS, CARD_SUIT)))
            if (user_suit_card == 'Red' and my_card[1] in red) or (user_suit_card == 'Black' and my_card[1] in black):
                print("Поздравляю! Ты выиграл! Загадана карта:", my_card[0] + my_card[1])
                return
            else:
                print('Неправильно. Моя карта была:', my_card[0] + my_card[1])
                attempts -= 1
                print('Осталось попыток:', attempts)
        else:
            print('Введи, пожалуйста, корректную масть: red или black')

    print('У вас закончились попытки. Моя карта была:', my_card[0] + my_card[1])

def main():
    username, attempts = welcome_message()
    play_game(attempts)

if __name__ == "__main__":
    main()
