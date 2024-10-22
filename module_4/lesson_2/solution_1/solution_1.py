import json


with open('sales.json', 'r', encoding="utf-8") as json_file:
    json_data= json.load(json_file)


def  calculation_revenue(data):
    """Функция обходит данные файла и складывает выручку одинаковых категорий товаров"""
    
    end_info = {}

    for sale in data['sales']:
        category = sale['category']
        total_price = sale['total_price'] * sale['quantity']

        if category not in end_info:    
            end_info[category] = total_price
        else:
            end_info[category] += total_price
    
    return end_info


result = calculation_revenue(json_data)

for category, total_prise in result.items():
    print(f"Выручка по категории: {category}: {total_prise}")
    

#Задание 1: Анализ продаж магазина
#Описание:

#Роман хочет проанализировать продажи своего магазина. 
#Данные о продажах хранятся в JSON-файле. 
#Каждая запись в файле содержит информацию о продаже товара: название, категорию, количество и общую стоимость.
#Реализуйте программу, которая читает данные из JSON-файла и подсчитывает общую выручку по каждой категории товаров.


#Пример содержимого файла sales.json:

{

  "sales": [

    {

      "product": "Футболка",

      "category": "Одежда",

      "quantity": 3,

      "total_price": 1500

    },

    {

      "product": "Чашка",

      "category": "Посуда",

      "quantity": 2,

      "total_price": 700

    }

    # Другие записи

  ]

}


#Пример работы программы
#Входные данные: *чтение из файла*
#Выходные данные: 
#Выручка по категории "Одежда": X 
#Выручка по категории "Посуда": Y 