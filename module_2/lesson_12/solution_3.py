data_sets = [
    ([10, 23, 35, 47], lambda x: x % 2 != 0),   # фильтр нечётных значений
    ([5, 7, 8, 10], lambda x: x > 7),  # больше 7
    ([1, 2, 3, 5, 6], lambda x: x < 5),    # меньше 5
    ([10, 20, 30, 40, 50], lambda x: x % 5 == 0 and x % 8 == 0) # кратные только 5 и 8
]

def filter_data(data, filter_func):
    return list(filter(filter_func, data))


for data, filter_func in data_sets:
    filtered_data = filter_data(data, filter_func)
    print(f"Отфильтрованные данные: {filtered_data}")


#Задача 3: Использование лямбда-функций для фильтрации данных
#Описание:  

#Для удобства анализа данных продаж Роман хочет использовать фильтрацию данных с помощью лямбда-функций. 
#Напишите функцию `filter_data`, которая принимает список значений и лямбда-функцию для фильтрации, и применяет эту лямбда-функцию для отбора данных. 
#Роман нанял программиста, но он не смог реализовать весь функционал. 

#data_sets = [

#   ([10, 23, 35, 47], # фильтрация нечётных значений),
#    ([5, 7, 8, 10], # значения больше 7),
#    ([1, 2, 3, 5, 6], # значения меньше 5),
#    ([10, 20, 30, 40, 50], # только значения, кратные 5 и 8)]

#for data, filter_func in data_sets:
#filtered_data = filter_data(data, filter_func)

#Подсказка: вместо комментариев должны быть лямбда функции
#Примеры входных и выходных данных (в данной задаче не нужно получать данные, допишите код представленный выше):

#| Входные данные      |            Выходные данные               |
#| ------------------  | -----------------------------------------|
#|                     | Отфильтрованные данные: [23, 35, 47]     |
#|                     | Отфильтрованные данные: [1, 2, 3]        |
#|                     | Отфильтрованные данные: [40]             |