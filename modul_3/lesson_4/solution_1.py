from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


class Guitar(ABC):
    def play(self):
        print("Гитара: воспроизводит звук")


class Piano(ABC):
    def play(self):
        print("Пианино: воспроизводит звук")


class Flute(ABC):
    def play(self):
        print("Флейта: воспроизводит звук")


my_guitar = Guitar()
my_piano = Piano()
my_flute = Flute()
my_guitar.play()
my_piano.play()
my_flute.play()


#Задание 1: Школа музыки (Наследование от абстрактного класса)
#Создайте абстрактный класс Instrument с абстрактным методом play().
#Создайте подклассы Guitar, Piano, и Flute, каждый из которых переопределяет метод play.
#В каждом подклассе должен быть своя реализация метода для воспроизведения звука инструмента.
#В главной программе создайте список объектов типа Instrument и вызовите для каждого метод play.