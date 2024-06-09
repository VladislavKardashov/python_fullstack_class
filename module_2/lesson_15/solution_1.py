def add_client(name, history):
    client_id = len(history) + 1
    history[client_id] = {'name': name, 'orders': []}


def make_order(client_id, history, order_details):
    history[client_id]['orders'].append(order_details)


def get_history(client_id, history):
    return history[client_id]['orders']


client_history = {}

add_client('Roman', client_history)
make_order(1, client_history, {'order_id': 1, 'amount': 100})


print(get_history(1, client_history))




#Задача 1: Исправление CRM-системы для магазина Романа
#Описание:

#Роман нанял разработчика для создания CRM-системы для своего магазина. 
#Однако, получив код, Роман обнаружил, что скрипт не запускается. 
#Ваша задача — проанализировать код, исправить синтаксические ошибки, добавить аннотации типов и привести имена функций в соответствие с PEP 8. 