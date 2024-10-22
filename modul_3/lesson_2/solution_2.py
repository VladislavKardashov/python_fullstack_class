from datetime import datetime

class Person:
    population: int = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, datetime.now().year - birth_year)

    def __str__(self) -> str:
        return f'Это {self.name}. Ему {self.age}.'

    @classmethod
    def display_population(cls) -> None:
        print(f"Население - {cls.population} чел.")

person1 = Person("Андрей", 29)
print(person1)
person2 = Person.from_birth_year("Олег", 36)
print(person2)
person3 = Person("Михаил", 24)
print(person3)

Person.display_population()


#Задание 2: Работа с атрибутами класса
#Добавьте в класс Person атрибут класса population, который будет отслеживать количество созданных экземпляров.
#Обновите методы __init__ и from_birth_year так, чтобы они увеличивали population на 1 при создании нового экземпляра.
#Создайте метод класса, который выводит текущую популяцию.