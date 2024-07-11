import telebot
from telebot import types
TOKEN = '6758417186:AAGt-9ZzLbempdTN8kg_LgczKEoC28ZU5SA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('3Д панель')
    item2 = types.KeyboardButton('Штакетник')
    item3 = types.KeyboardButton('Сварная сетка')
    item4 = types.KeyboardButton('Рабица')
    item5 = types.KeyboardButton('Обратная связь')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup) 

@bot.message_handler(content_types=['text'])
def bot_message(message):
        if message.chat.type == 'private':
            if message.text == '3Д панель':
                bot.send_message(message.shat.id,)
                back = types.KeyboardButton('Назад')
                markup.add(back)
            bot.send_message(message.chat.id, '3Д панель', reply_markup = markup) 
       
        elif message.text =='Штакетник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('7,5')
            item2 = types.KeyboardButton('10')
            item3 = types.KeyboardButton('10,5')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Штакетник', reply_markup = markup) 
        
        elif message.text =='Сварная сетка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            bot.send_message(message.chat.id, 'Сварная сетка', reply_markup = markup) 

        elif message.text =='Рабица':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            bot.send_message(message.chat.id, 'Рабица', reply_markup = markup) 

        elif message.text =='Обратная связь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            bot.send_message(message.chat.id, 'Обратная связь', reply_markup = markup) 

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('3D панель')
            item2 = types.KeyboardButton('Штакетник')
            item3 = types.KeyboardButton('Сварная сетка')
            item4 = types.KeyboardButton('Рабица')
            item5 = types.KeyboardButton('Обратная связь')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'Назад', reply_markup = markup) 



bot.polling(none_stop = True)  