import random

import telebot

API_TOKEN = "6681988632:AAGglwtiraGuUE_LujKgCkQpEW3omf6Az2w"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def start_help(message: telebot.types.Message):
    text = "Привет! Я помогу тебе подобрать фильм!\n\n"\
           "/get_film - получить фильм на вечер\n"
    bot.send_message(message.chat.id,text)


@bot.message_handler(commands=["get_film"])
def get_film(message: telebot.types.Message):
    with open("films.txt", "r", encoding="utf-8") as file:
        films = file.read().split("\n")
    film = random.choice(films)
    bot.send_message(message.chat.id, text=f"Сугодня вечером стоит посмотреть{film}")


print("Бот запущен")
bot.infinity_polling()



