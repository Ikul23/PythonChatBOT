import telebot
from random import choice

TOKEN = "6436320511:AAFR1NDJu2Aj0QjALiYRUN6bvpq9spKQewQ"

bot = telebot.TeleBot(TOKEN) # авторизация бота

@bot.message_handler(commands=["start"])
def start(message):
  keyboard = telebot.types.ReplyKeyboardMarkup()
  red_button = telebot.types.KeyboardButton("🟥")
  black_button = telebot.types.KeyboardButton("⬛️")
  keyboard.row(red_button)
  keyboard.row(black_button)
  bot.send_message(message.chat.id,
                   "What is the card's suit color: 🟥 or ⬛️",
                   reply_markup=keyboard)

  bot.register_next_step_handler(message, answer_card)


def answer_card(message):
  random_card_number, random_card_suit = generate_random_card()
  if message.text == "🟥" and random_card_suit in ["H", "D"]:
    bot.send_message(
        message.chat.id,
        "Correct! The card was: " + random_card_number + random_card_suit)
  elif message.text == "⬛️" and random_card_suit in ["C", "S"]:
    bot.send_message(
        message.chat.id,
        "Correct! The card was: " + random_card_number + random_card_suit)
  else:
    bot.send_message(
        message.chat.id,
        "Incorrect! The card was: " + random_card_number + random_card_suit)

  start(message)


def generate_random_card():
  card_number = choice(
      ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
  card_suit = choice(["H", "D", "S", "C"])
  return [card_number, card_suit]


bot.infinity_polling()