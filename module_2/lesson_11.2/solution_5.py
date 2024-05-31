month_len_1 = 30
month_len_2 = 31

def sales_schedule_with_range(month_len):
    return list(range(3, month_len + 1, 3))

month_1 = sales_schedule_with_range(month_len_1)
month_2 = sales_schedule_with_range(month_len_2)

print(f"Дни распродажи: {month_1}")
print(f"Дни распродажи: {month_2}")


#Задача 5: Расписание распродаж
#Описание:

#Для улучшения управления запасами Роман решил устроить распродажу каждый третий день месяца. 
#Напишите функцию `sales_schedule_with_range`, которая принимает количество дней в месяце и использует `range` для создания и вывода списка дней, когда будет распродажа.