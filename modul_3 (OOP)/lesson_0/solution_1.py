from typing import Literal 

class Animal:
    def __init__(  
            self, 
            animal_type: str,
            animal_sound: str,
            view: Literal["хищное", "травоядное"]
    ):
        self.animal_type = animal_type
        self.animal_sound = animal_sound
        self.view = view

    def __str__(self) -> str: 
        return f'Это {self.view} животное {self.animal_type}!'
    
    def sound(self) -> str:
        return f"{self.animal_type} издает следующие звуки {self.animal_sound}"
    
tiger = Animal("Тигр", "РрРрРр", "Хищное")
zebra = Animal("Зебра", "Ква-Ха", "Травоятное")

print(tiger, tiger.sound())
print(zebra, zebra.sound())


#Задание:
#Создайте класс, Animal у которого будут методы: издавать звуки и кушать. 
#А при создании мы сможем передавать название животного, которое мы хотим создать и что оно “говорит”.