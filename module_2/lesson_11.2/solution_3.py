def track_low_stock_with_for(stock: dict, stock_level):
    for product, item in stock.items():
        if item < stock_level:
            print('Низкий запас: ')
            print(f'{product} - {item}')

track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)






#Задача 3: Отслеживание запасов
#Описание:

#Роман хочет знать, какие товары скоро закончатся на складе. 
#Напишите функцию `track_low_stock_with_for`, которая принимает словарь с товарами и их количеством, 
#использует цикл `for` для идентификации товаров с количеством меньше заданного порога и выводит их в формате "Товар - Количество", 
#каждого товара в отдельной строке.