products_list = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

product_min = min(products_list, key=lambda x: products_list [x])
product_max = max(products_list, key=lambda x: products_list [x])

print(f"Самый дешевый товар: {products_list} - {products_list[product_min]} p.")
print(f"Самый дорогой товар: {products_list} - {products_list[product_max]} p.")



#Задача 3: Минимальная и максимальная цена
#Описание:

#Роман хочет определить самый дешевый и самый дорогой товар в магазине. 
#Данные для словаря: {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}. 
#Программа должна вывести название и цену самого дешевого и самого дорогого товара.