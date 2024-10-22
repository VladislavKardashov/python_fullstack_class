import json
import csv
from datetime import datetime, date
import re

class Client:
    def __init__(self, name, surname, birthday, bonuses):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    @staticmethod
    def verification_client(name, surname, birthday, bonuses):
        """Проверка клиента по необходимым параметрам."""
        
        
        if not (0 <= bonuses <= 10000000):
            return False

        
        if not (re.match(r'^[А-Яа-яЁё\s]+$', name) and re.match(r'^[А-Яа-яЁё\s]+$', surname)):
            return False
        
        try:
            
            birth_date = datetime.strptime(birthday, '%d.%m.%Y').date()
            current_date = date.today()
            if birth_date > current_date or birth_date.year < 1950:
               return False
        except ValueError:
            return False

        return True
    
def cvs_to_json(file):
    """Функция для переформатирования данных из csv файла в json."""
    processed_rec = 0   
    missing_rec = 0     

    with open(file, 'r', encoding='utf-8') as csv_file: 
        csv_reader = csv.DictReader(csv_file)

        clients = [] 
        for row in csv_reader:
            try:
                name = row['Name'].lower()
                surname = row['Surname'].lower()
                birthday = row['Birthday']
                bonuses = int(row['Bonuses'])

                if Client.verification_client(name, surname, birthday, bonuses):  
                    clients.append({
                        'name': name,
                        'surname': surname,
                        'birthday': birthday,
                        'bonuses': bonuses
                    })
                    processed_rec += 1

                else:
                    missing_rec += 1

            except (ValueError, KeyError):
                missing_rec += 1

    with open('clients.json', 'w', encoding='utf-8') as json_file: 
        json.dump({'clients': clients}, json_file, ensure_ascii=False, indent=2)

    
    print(f'Было обработано(клиентов): {processed_rec} \nБыло пропущено(клиентов): {missing_rec}')


cvs_to_json('clients.csv')


#Задание 3: Упаковка клиентов
#Роман решил подключить CRM систему для обработки данных о клиентах. 
#Данные необходимо отправлять в CRM систему в виде json файлов. 
#На стороне CRM системы нет проверки данных, поэтому необходимо проверять данные до отправки. 
#Данные о клиентах уже хранятся в файле clients.csv.

#Реализуйте программу, которая будет переформатировать данные из csv файла в json. Для дальнейшего расширения программы реализуйте класс Client атрибутами которого будут поля csv файла, а методами класса реализуйте проверки:
#Имя и фамилия: должны быть строками содержащими только символы кириллицы
#Дата рождения: должна быть датой от 1950 до текущей даты(date.today())
#Бонусы: должны быть целым числом, от 0 до 10 000 000
#Если какое то значение указано неверно всю строку необходимо пропустить. В конце работы программы выведите число пропущенных и обработанных записей.

#Структура файлов:
#clients.csv:
#Name,Surname,Birthday,Bonuses
#Роман,Горбачёв,28.01.1989,9999999 

#clients.json:

{

 "clients": [

   {

     "name": "as",

     "surname": "",

     "birthday": "28.01.1989",

     "Bonuses": 9999999

   }

 ]

}


#Пример работы программы
#Входные данные: *чтение из файлов*
#Выходные данные: 
#Было обработано(клиентов): 10 
#Было пропущено(клиентов) : 1 