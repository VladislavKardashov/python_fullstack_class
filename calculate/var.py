import telebot
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('3Д панель')
    item2 = types.KeyboardButton('Штакетник')
    item3 = types.KeyboardButton('Сварная сетка')
    item4 = types.KeyboardButton('Обратная связь')

    markup.add(item1, item2, item3, item4)
    
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['3Д панель'])
def text(message):
    length = input('Введите длину: м')
    panel = 2.5
    result = int(length) / panel
    pillars = int(result) + 1
    print(f'Для заданной длинны потребуется {result} панелей!')
    print(f'Для заданного участка потребуется {pillars} столбов')

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('назад')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Приступим!', reply_markup=markup)


@bot.message_handler(commands=['Штакетник'])
def text(message):
    markup = types.InlineKeyboardMarkup() 
    btn1 = types.InlineKeyboardButton('76 мм')
    btn2 = types.InlineKeyboardButton('100 мм')
    markup.row(btn1, btn2)

    gap = input('Введите желаемый зазор: мм')
    length = input('Введите длину забора: мм')
    width_1 = float(btn1) + gap
    width_2 = int(btn2) + gap
    result_1 = float(length) / width_1
    result_2 = int(length) / width_2
    print(f'Для заданной длинны потребуется {result_1} штакетин!')
    print(f'Для заданного участка потребуется {result_2} штакетин!')
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('назад')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Приступим!', reply_markup=markup)
    

@bot.message_handler(commands=['Сварная сетка'])
def text(message):
    bot.send_message(message.chat.id, message.text)
    length = input('Введите длину: м')
    roll = 15
    result = int(length) / roll
    print(f'Для заданной длинны потребуется {result} панелей!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('назад')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Приступим!', reply_markup=markup)   



def on_click(message):
    if message.text == 'Обратная связь':
        bot.send_message(message.chat.id, 'Опишите возникшие сложности')
    elif message.text == 'Удалить':
        bot.send_message(message.chat.id, 'Delete')

# Не нашел как сделать обратную связь, что бы написанные сообщения, отправлялись мне (Нашел толшько в аирограмме, но это не подходит)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)