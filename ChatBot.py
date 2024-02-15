import random

username = input("Введите ваше имя: ")

print('Приятно познакомиться, ' + username + '!')

print(username + ', давай сыграем в игру "Угадай масть". Я загадаю игральную карту, а ты угадаешь ее масть!')

CARD_SUIT = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
CARD_NUMBERS = ['2', '3', '4', '5', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

red = ['Diamonds', 'Hearts']
black = ['Spades', 'Clubs']

while True:
    user_suit_card = input('Введи масть загаданной мною карты:\n ').capitalize()

    if user_suit_card == 'Red' or user_suit_card == 'Black':
        break
    else:
        print('Введи, пожалуйста, корректную масть: red или black')

my_card = random.choice(list(zip(CARD_NUMBERS, CARD_SUIT)))
print("Мной загадана карта:", my_card[0] + my_card[1])

if user_suit_card == 'Red' and my_card[1] in red:
    print('Ты выиграл!')
elif user_suit_card == 'Black' and my_card[1] in black:
    print('Ты выиграл!')
else:
    print('Ты проиграл!')
