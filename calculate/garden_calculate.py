from telebot import TeleBot
from telebot import types
from telebot.types import Message
from dotenv import load_dotenv
import os

load_dotenv(".env")
TG_TOKEN = os.getenv("TG_TOKEN")

bot = TeleBot(TG_TOKEN)

tasks: list[list[str]] = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('3Д панель')
    item2 = types.KeyboardButton('Штакетник')
    item3 = types.KeyboardButton('Сварная сетка')
    item4 = types.KeyboardButton('Рабица')
    item5 = types.KeyboardButton('Обратная связь')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '3Д панель':
            bot.send_message(message.shat.id, )
            back = types.KeyboardButton('Назад')
            markup.add(back)
        bot.send_message(message.chat.id, '3Д панель', reply_markup=markup)
        
        L = input("Введите длину: м")
        panel = int(2,5)
        result = L / panel 
        print(f"Итого панелей: {result} шт")

        

    elif message.text == 'Штакетник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('76 мм')
        item2 = types.KeyboardButton('10')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, back)


        L = input("Введите длину: мм")
        gap = input("Введите зазор между: мм")
        light_1 = int(item1) + gap
        light_2 = int(item2) + gap
        result_1 = L / light_1
        result_2 = L / light_2
        print(f"Штакетин : {result_1}")
        print(f"Штакетин : {result_2}")



    elif message.text == 'Сварная сетка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)

        L = input("Введите длину: м")
        roll = int(15)
        result = L / panel 
        print(f"Итого панелей: {result} рулонов")



    elif message.text == 'Обратная связь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)
     # Не нашел как сделать обратную связь, что бы написанные сообщения, отправлялись мне (Нашел толшько в аирограмме, но это не подходит)

        bot.send_message(message.chat.id, 'Обратная связь', reply_markup=markup)
        

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('3D панель')
        item2 = types.KeyboardButton('Штакетник')
        item3 = types.KeyboardButton('Сварная сетка')
        item4 = types.KeyboardButton('Рабица')
        item5 = types.KeyboardButton('Обратная связь')

        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


bot.polling()