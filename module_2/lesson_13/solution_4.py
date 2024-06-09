def validate_input(func):
    def wrapper(*args, **kwargs):
        if len(args) != 2 and len(kwargs) != 0:  
            raise ValueError("Колличество задач")

        if not isinstance(args[0], str):  
            raise TypeError("Название проекта должно быть строкой")

        if not isinstance(args[1], int): 
            raise TypeError("Второй аргумент не число!")

        return func(args)

    return wrapper


@validate_input
def estimate_time(args):
    result = "Estimated time calculated successfully"
    return result


try:
    project_1 = estimate_time("Веб-сайт", "пять")
    print(project_1)
except ValueError as ve:
    print(f"Ошибка: {ve}")
except TypeError as te:
    print(f"Ошибка: {te}")


try:
    project_2 = estimate_time("Визитка", 10)
    print(project_2)
except ValueError as ve:
    print(f"Ошибка: {ve}")
except TypeError as te:
    print(f"Ошибка: {te}")


#Задание 4: Валидация входных данных для расчёта сроков
#Описание:

#Функция `estimate_time` используется для расчёта времени выполнения проекта. 
#Роман хочет быть уверенным, что в функцию подаются данные правильного типа (название проекта - строка, количество задач - целое число), и в противном случае получать соответствующее предупреждение. 
#Сначала проверяется количество аргументов, потом тип первого и затем тип второго аргумента.