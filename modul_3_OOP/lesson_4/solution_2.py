from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: str):
        pass


class TextFileHandler(FileHandler):
    def __init__(self, text_file):
        self.text_file = text_file

    def read(self):
        with open(self.text_file, 'r') as file:
            content = file.read()
            print(f"Текстоввй файл прочитан: {content}")

    def write(self, data: str):
        with open(self.text_file, "w") as file:
            file.write(data)
            print("Текстовый файл записан")


class BinaryFileHandler(FileHandler):
    def __init__(self, text_file):
        self.text_file = text_file

    def read(self):
        with open(self.text_file, 'rb') as file:
            content = file.read()
            print(f"Бинарный файл прочитан: {content}")

    def write(self, text_title):
        with open(self.text_file, "wb") as file:
            file.write(text_title.encode('utf-8'))
            print("Бинарный файл записан")


def save_data(handler: FileHandler, data: str):
    handler.write(data)
    handler.read()


text_handler = TextFileHandler("text.txt")
binary_handler = BinaryFileHandler("binar.bin")
save_data(text_handler, "Вперед, ни шагу назад!")
save_data(binary_handler, "Вперед, ни шагу назад!")


#Задание 2: Работа с файлами (Использование протоколов)
#Создайте протокол FileHandler с методами read() и write(data: str).
#Реализуйте два класса, TextFileHandler и BinaryFileHandler, которые реализуют этот протокол.
#TextFileHandler должен читать и писать текстовые файлы, а BinaryFileHandler — бинарные файлы. В реализации не обязательно действительно использовать файлы, но вы можете добавить такой функционал. В качестве решения достаточно вывести информацию, что файл был прочитан и записан
#Создайте функцию save_data(handler: FileHandler, data: str), которая сохраняет данные, используя переданный "обработчик файлов".