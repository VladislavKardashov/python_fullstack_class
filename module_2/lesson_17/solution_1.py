list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 2

def find_element(list, value):
    if list.count(value) > 0:
            return True
    return False

print(find_element(list, value))