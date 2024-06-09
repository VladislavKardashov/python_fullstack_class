cash = {
    'args': None,
    'result': None
}  

def check_args(func):
    def wrapper(*args):
        
        if cash['args'] == args:
            return f"Загрузили из кэша: {cash['result']}"
        else:
            result = func(*args)
            cash['args'] = args
            cash['result'] = result
            return f"Посчитали цену: {result}"

    return wrapper

@check_args
def calculate_project_cost(*args):
    return 3000


print(calculate_project_cost(('Логотип', 'Малый бизнес')))
print(calculate_project_cost(('Логотип', 'Малый бизнес')))




#Задание 3: Кеширование результатов расчёта стоимости проектов
#Описание:  

#Роман использует функцию `calculate_project_cost` для оценки стоимости проектов. 
#Однако расчёт требует значительных ресурсов. 
#Роман еще не знает про возможности кеширования. 
#Помогите Роману кэшировать результаты, чтобы повторные вызовы с теми же параметрами не требовали дополнительных вычислений.