def binari_find_element(my_list: list[int], element: int):
    if len(my_list) == 0:
        return False
    while True:
        central_element = my_list[len(my_list) // 2]
        if element == central_element:
            return True
        elif element > central_element and len(my_list) > 1:
            my_list = my_list[my_list.index(central_element):]
        elif element < central_element and len(my_list) > 1:
            my_list = my_list[:my_list.index(central_element)]
        else:
            return False

print(binari_find_element([2, 7, 14, 16, 20, 23, 26, 30, 35], 27))
print(binari_find_element([2, 7, 14, 16, 20, 23, 26, 30, 35], 25))
print(binari_find_element([2, 7, 14, 16, 20, 23, 26, 30, ], 27))
print(binari_find_element([2, 7, 14, 16, 20, 23, 26, 30, ], 25))
print(binari_find_element([], 0))



#Задание 2. (со звездочкой)

#Напишите функцию binary_find_element(), которая принимает на вход, список значений типа int и элемент. Предполагая, что список на входе отсортирован от меньшего к большему, проверьте в нем наличие элемента по следующему алгоритму:

#выставляем две переменные типа int в границы списка, индекс 0 и индекс последнего элемента.
#находим центральный (или один из двух центральных) элемент между двух границ.
#если наш элемент равен центральному – мы его нашли, возвращаем True.
#если он больше – сдвигаем левую границу до центра, продолжаем поиск в этой половине (повторяем все пункты, начиная со второго, для новых границ).
#если он меньше – сдвигаем правую границу до центра и продолжаем поиск в этой половине.
#если по итогу левая и правая границы сошлись, а элемент так и не найден – возвращаем False.
#Протестируйте свой алгоритм на списках нулевой, а также разной четной и нечетной длины.