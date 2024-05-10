input_prices = input("Список цен: ")
price = [int(x) for x in input_prices.split(', ')]

def find_max_price(price):
    if len(price) == 0:
        return None
    elif len(price) == 1:
        return price[0]
    else:
        max_price = find_max_price(price[1:])
        return price[0] if price[0] > max_price else max_price

result = find_max_price(price)

print(result)


#Задача 6: Поиск максимального элемента
#Описание:

#Роман хочет найти самый дорогой товар в одном из своих магазинов. 
#У него есть список цен товаров, но к сожалению, его программы не могут использовать встроенные функции Python для поиска максимального элемента. 
#Напишите рекурсивную функцию `find_max_price`, которая принимает на вход список цен и возвращает максимальную цену.