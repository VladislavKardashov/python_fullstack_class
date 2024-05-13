def calculate_discount(price, index=0, previous_price = None):
    price_end = []
    if index < len(price):
        new_price = price[index]
        new_discount = previous_price * 0.1 if previous_price is not None else 0
        discount_price = int(new_price - new_discount if previous_price is not None else new_price)
        price_end.append(discount_price)
        price_end += calculate_discount(price, index + 1, new_price)
    return price_end

price = [1000, 2000, 3000]

discount = ', '.join(map(str, calculate_discount(price)))
print("Выходные данные:", discount)


#Задача 7: Расчет скидок
#Описание:

#В дизайн-студии Романа каждый новый заказ получает скидку, размер которой равен 10% от стоимости предыдущего заказа. 
#Напишите рекурсивную функцию `calculate_discount`, которая принимает на вход список стоимостей заказов и возвращает список стоимостей заказов уже со скидками.