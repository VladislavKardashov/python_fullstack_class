product_list = {'Яблоко': 100,'Банан': 80,'Кофе': 250,'Чай': 150}
    
product = input("Введите название товара: ")

if product in product_list:
    print("Цена: ", product_list[product])
else:
    print("Товар отсутствует.")



#Задача 1: Словарь цен
#Описание:
    
#Роман имеет магазин и хочет быстро узнать стоимость определенных товаров. 
#Данные для словаря: {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}.
#Пользователь вводит название товара, и программа должна вывести его цену.