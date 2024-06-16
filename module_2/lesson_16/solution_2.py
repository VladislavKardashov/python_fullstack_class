input_length = input("Введите длины полок: ")
length_shelves = [int(x) for x in input_length.split(",")] # конвертация введенных данных input_length в список длинн полок

input_items = input("Введите количесво товара: ")
item_quantity = [int(x) for x in input_items.split(",")]# конвертация введенных данных input_items в список с кол-вом товара для каждой полки

def create_shelves(length_shelves, item_quantity):

    shelves = [[length, quantity] for length, quantity in zip(length_shelves, item_quantity)]
    return shelves

finished_shelves = create_shelves(length_shelves, item_quantity)


print(f"Полки: {finished_shelves}")


#Задача 2: Распределение товаров по полкам
#Описание:  

#Теперь, когда у Романа есть массив полок, он хочет добавить информацию о количестве товаров на каждой полке. 
#Напишите программу, которая модифицирует каждый подмассив, заменяя 0 на количество товаров, введенное пользователем.


#Таблица входных и выходных данных:

#|         Входные данные         |          Выходные данные           |
#| ------------------------------ | ---------------------------------- |
#| Полки: 4, 5, 6,                |    Полки: [[4, 2], [5, 3], [6, 5]] |
#| Кол-во товаров: 2,3,5          |                                    |
#| Полки: 3, 4                    |    Полки: [[3, 1], [4, 4]]         |
#| Кол-во товаров: 1,4            |                                    |