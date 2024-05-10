worker_dict = {
    "Анна" : 5,
    "Боб" : 7,
    "Сюзан" : 9,
    "Джон" : 1,
    "Майк" : 1,
    "Эмили" : 1
}

def responsible_worker(worker_dict):
    names_worker = list(worker_dict.keys())
    values_worker = list(worker_dict.values())

    max_copleted = max(values_worker)
    responsible_worker = [name for name, completed in worker_dict.items() if completed == max_copleted]

    return responsible_worker

responsible_worker = responsible_worker(worker_dict)
result = ', '.join(map(str, responsible_worker))

print("Самый ответственный сотрудник: ", result)


#Задание 3: Ответственный сотрудник 🔥
#Описание:

#Роман хочет знать, какой из его сотрудников в студии дизайна наиболее ответственный в этом месяце. 
#Напишите функцию, которая принимает количество задач, выполненных каждым сотрудником, и возвращает имя самого ответственного.

#Функция должна быть реализована без использования циклов. 
#Но можно использовать list comprehension.