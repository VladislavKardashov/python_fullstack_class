from typing import Literal


class Animal:
    def __init__(
            self,
            animal_type: str,
            feeds: Literal['травоядное', 'хищное'],
            animal_sound: str,
    ):
        self.animal_type = animal_type
        self.feeds = feeds
        self.animal_sound = animal_sound

    def __str__(self) -> str:
        return f'Это {self.feeds} животное {self.animal_type}!'

    def sound(self) -> str:
        return f'{self.animal_type} издает звуки {self.animal_sound}!'

    def feed(self) -> str:
        return f'{self.animal_type} кушает {self.feeds}!'


tiger = Animal('тигр', 'хищное', 'ррр')

print(tiger, tiger.sound())
print(tiger, tiger.feed())

zebra = Animal("зебра", 'травоядное', 'ква-ха')

print(zebra, zebra.sound())
print(zebra, zebra.feed())




#Задание:
#Создайте класс, Animal у которого будут методы: издавать звуки и кушать. 
#А при создании мы сможем передавать название животного, которое мы хотим создать и что оно “говорит”.