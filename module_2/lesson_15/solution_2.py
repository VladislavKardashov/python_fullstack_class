def update_stock(item, quantity, stock):
    if item in stock:
        stock[item]['quantity'] += quantity
    else:
        stock[item] = {'quantity': quantity}


def get_item_quantity(item_name, stock):
    return stock[item_name]['quantity']


def remove_item(item, stock):
    if item in stock:
        del stock[item]


stock = {}


update_stock('Apple', 50, stock)
update_stock('Banana', 30, stock)
update_stock('Coffee', 20, stock)


print(get_item_quantity('Apple', stock))


remove_item('Banana', stock)


print(stock)



#Задача 2: Код-ревью для Романа
#Описание:

#Роман подумал, что много денег тратит на разработчиков, которые “просто нажимают на кнопки”, он сам написал систему учёта остатков. 
#Однако, код не запустился и он просит вас провести код ревью его кода.