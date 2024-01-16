shop = "Desing"
slogan = input("Введите описание: ")
number_of_occurrences = 0

shop_index = slogan.find(shop)

while shop_index != -1:
    umber_of_occurrences += 1
    shop_index = slogan.find(shop, shop_index +1)

print(f"Количество входов: {number_of_occurrences}")

#Задание 4: Подсчет частоты вхождений
#Описание:

#Роман интересуется, сколько раз слово "Design" теперь встречается в различных новых описаниях.