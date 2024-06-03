def collect_data():
    return process_data(data)

import statistics

def process_data(data):
    average = statistics.mean(data)
    return summarize_data(average)

def summarize_data(average):
    return f"Итого: Среднее значение: {average}"

data = [1, 2, 3, 4, 5]
data = [10, 15, 5, 20]
result = collect_data()
print(result)


#Задача 1: Цепочка функций обработки данных
#Описание: 

#Роман реализует систему аналитики для магазинов. 
#Создайте три функции: `collect_data`, `process_data` и `summarize_data`. 
#Функция `process_data` должна принимать результат работы `collect_data` как аргумент, а `summarize_data` должна принимать результат работы `process_data`.

#Примеры входных и выходных данных:

#|      Входные данные     |        Выходные данные       | 
#| ----------------------- | -----------------------------|
#| Данные: [1, 2, 3, 4, 5] | Итог: Среднее значение: 3    |
#| Данные: [10, 15, 5, 20] | Итог: Среднее значение: 12.5 |

#Примечание:
#`collect_data` собирает данные и вызывает функцию`process_data`
#`process_data` находит среднее значение и вызывает `summarize_data`, 
#summarize_data` создает отчет