items_price = input("Введите цены на товары и размер скидки: ")
price_list = [int(x) for x in items_price.split (', ')]

def calculate_discount(price):
    price_list = price[:-1]
    sum_of_price = sum(price_list)
    discount = sum_of_price * (price[-1]/100)
    return discount

total = calculate_discount(price_list)

print(f"Сумма скидки: {total}")


#Задача 1: Подсчет скидки
#Описание:

#Роман хочет узнать, какую сумму он сэкономит покупателям, если предложит скидку на товары в его магазине. 
#Напишите функцию `calculate_discount`, которая принимает на вход список цен товаров и процент скидки, при вводе скидка будет последним числом. 
#Функция должна возвращать сумму скидки на все товары.