order_1 = {'id': 1, 'items': ['book', 'pen']}
order_2 = {'id': 2, 'items': []}

def check_order(check: dict):
    return bool(check.get('items'))

def package_order(check):  
    return f"Отправка: Заказ упакован {check.get('id')}"

def send_order(check_function, package_order, check: dict):
    if check_function(check):
        return package_order(check)
    else:
        return f"Отправка: Заказ {check.get('id')} пуст"

print(send_order(check_order, package_order, order_1))
print(send_order(check_order, package_order, order_2))


#Задача 2: Композиция функций для обработки заказов
#Описание:  

#В рамках оптимизации работы интернет-магазина Роман хочет создать функционал для комплексной обработки заказов. 
#Разработайте три функции: `check_order`, `package_order` и `send_order`. 
#Функция `send_order` должна принимать `check_order` и `package_order` и применять `package_order` к результату выполнения `check_order`.
#Примеры входных и выходных данных:

#|      Входные данные         |        Выходные данные     |
#| ------------------------    | ---------------------------|
#| id: 1, items: 'book', 'pen' | Отправка: Упакован заказ 1 |
#| id: 2, items:               | Отправка: Заказ 2 пуст     |

#Примечание:

#`check_order` проверяет заказ, `package_order` упаковывает его, 
#`send_order` координирует процесс и инициирует отправку. 
#Функиция `send_order` не должна начинать упаковку заказа, если он пустой!



#В нашем примере вызов функции должен выглядеть так:
#order1 = {'id': 1, 'items': ['book', 'pen']}
#order2 = {'id': 2, 'items': []}


#print(send_order(check_order, package_order, order1))
#print(send_order(check_order, package_order, order2))