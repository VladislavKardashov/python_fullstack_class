products_roster = {
    'Яблоко' : 100,
    'Банан' : 80,
    'Кофе' : 250,
    'Чай' : 150
}

product_min = min(products_roster, key=lambda x: products_roster[x])
product_max = max(products_roster, key=lambda x: products_roster[x])

print(f"Самый дешевый: {product_min} - {products_roster[product_min]} руб.")
print(f"Самый дорогой: {product_max} - {products_roster[product_max]} руб.")



#Задача 3: Минимальная и максимальная цена
#Описание:

#Роман хочет определить самый дешевый и самый дорогой товар в магазине. 
#Данные для словаря: {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}. 
#Программа должна вывести название и цену самого дешевого и самого дорогого товара.