import json

with open('inventory.json', 'r') as json_file:
    json_data = json.load(json_file)

def product_quantity(data):
    """функция проверяет наличие товаров и сосволяет список покупок"""

    shop_list = {}

    for material in data['inventory']:
        item = material['item']
        quantity = material['quantity']
        min_required = material['minimum_required']
        required = min_required - quantity

        if item not in shop_list:
            if quantity < min_required:
                shop_list[item] = required
        
    return shop_list


result = product_quantity(json_data)


for item, required in result.items():
    print(f"Необходимо закупить: {item} {required} шт.")




#Задание 2: Управление запасами дизайн-студии
#Роман хочет оптимизировать закупки в дизайн-студии. 
#Данные о материалах и инструментах хранятся в формате JSON.
#Создайте программу, которая анализирует данные о запасах из JSON-файла и выводит список материалов, 
#которые необходимо закупить (если их количество меньше минимально необходимого).



#Пример содержимого файла inventory.json:

{

  "inventory": [

    {

      "item": "Кисти",

      "category": "Инструменты",

      "quantity": 5,

      "minimum_required": 10

    },

    {

      "item": "Краска акриловая",

      "category": "Материалы",

      "quantity": 20,

      "minimum_required": 15

    }

    # Другие записи

  ]

}


#Пример работы программы
#Входные данные: *чтение из файла*
#Выходные данные: 
#Необходимо закупить: Кисти 5 шт.