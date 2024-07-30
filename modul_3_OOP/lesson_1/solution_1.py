class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)

    def __getitem__(self, index):
        return self.books[index]

    def __contains__(self, title):
        for book in self.books:
            if book['title'] == title:
                return True
        return False

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        return self

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
        return self

library = Library()
library.add_book('Руслан и Людмила', 'Пушкин А.С.').add_book('Война и мир', 'Толстой Л.Н.').add_book('Мастер и Маргарита', 'Булгаков М.А.').remove_book('Мастер и Маргарита')
print(library.books)

library.remove_book('Война и мир')
print(library.books)

print('Руслан и Людмила' in library)

print(library[0:])

#Задание

#Создайте класс Library, который будет содержать список книг. Каждая книга должна иметь название и автора.
#Реализуйте метод add_book, который добавляет книгу в библиотеку.
#Реализуйте метод remove_book, который удаляет книгу из библиотеки по названию.
#Используйте магический метод __getitem__ для получения книги по индексу.
#Используйте методы __contains__ для проверки, есть ли книга в библиотеке по названию.
#Реализуйте методы цепочки для добавления и удаления книг (например, add_book().remove_book().add_book()).