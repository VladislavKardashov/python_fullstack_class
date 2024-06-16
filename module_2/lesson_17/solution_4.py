def sort_objects(list_dict, key):
    list_dict.sort(key=lambda x: x[key])
    return list_dict

people_book = [
    {"nike": 73286514, "age": 258, "lori": 4},
    {"age": 6, "harry potter": 985474, "rogi": 1},
    {"lieber": 366586054, "din": 7, "age": 7536,},
    {"age": 54, "pies": 1586514, "khvost": 4},
    {"dog": 1456514, "snake": 1, "age": 20}
]

key = "age"

print(people_book)

sort_objects(people_book, key)

for person in people_book:
    print(person)



#Задание 4.

#В Python есть встроенная функция сортировки, которая позволяет отсортировать элементы, например, в списке.
#Реализуйте на ее основе функцию sort_objects(), которая принимает два аргумента:

#Список, содержащий словари с ключами-строками и значениями-целыми числами.
#Строковый ключ (гарантированно присутствующий в каждом словаре из списка).
#Эта функция должна возвращать такой же список из словарей, только отсортированный по значению, которое в каждом словаре хранится по переданному строковому ключу.