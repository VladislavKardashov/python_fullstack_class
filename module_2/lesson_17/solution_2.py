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