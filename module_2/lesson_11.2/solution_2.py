def count_specific_items_with_while(products: list, product):
    m = 0
    e = 0
    while e < len(products):
        if products[e] == product:
            m += 1

        e += 1
    print(f"Колличество '{product}': {m}")


count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy'], 'toy')
count_specific_items_with_while(['clotes', 'clotes', 'clotes'], 'clotes')


#Задача 2: Подсчет определенных товаров
#Описание:

#В магазинах Романа есть различные категории товаров. 
#Необходимо написать функцию `count_specific_items_with_while`, которая с помощью цикла `while` подсчитывает количество товаров определенной категории в переданном списке.
#Ограничения:
#- Использовать только цикл `while`
