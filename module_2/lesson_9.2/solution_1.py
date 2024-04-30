def calculate_discount(prices):
    discount_percentage = prices[-1]
    total_discount = 0 

    for prices in prices[:-1]
        discount = price * discount_percentage / 100
        total_discount += discount

    return total_discount

prices = [100, 200, 300, 10]
discount = calculate_discount(prices)
print("Сумма скидки на все товары:", int(discount))

prices = [50, 150, 250, 20]
discount = calculate_discount(prices)
print("Сумма скидки на все товары:", int(discount))


#Задача 1: Подсчет скидки
#Описание:

#Роман хочет узнать, какую сумму он сэкономит покупателям, если предложит скидку на товары в его магазине. 
#Напишите функцию `calculate_discount`, которая принимает на вход список цен товаров и процент скидки, при вводе скидка будет последним числом. 
#Функция должна возвращать сумму скидки на все товары.