input_numer = input("Список цен: ")
numer = [int(x) for x in input_numer.split(', ')]

def calculate_discount(numer, index = 0, first_numer = None):
    numer_1 = []

    if index < len(numer):
        next_numer = numer[index]
        numer_discount = first_numer * 0.1 if first_numer is not None else 0
        new_numer = int(next_numer - numer_discount if first_numer is not None else next_numer)
        numer_1.append(new_numer)
        numer_1 += calculate_discount(numer, index + 1, next_numer)
    return numer_1


result = calculate_discount(numer)
result_int = [int(x) for x in result]

print("Выходные данные:", result)


#Задача 7: Расчет скидок
#Описание:

#В дизайн-студии Романа каждый новый заказ получает скидку, размер которой равен 10% от стоимости предыдущего заказа. 
#Напишите рекурсивную функцию `calculate_discount`, которая принимает на вход список стоимостей заказов и возвращает список стоимостей заказов уже со скидками.