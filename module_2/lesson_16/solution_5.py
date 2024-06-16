from itertools import count


def distances(n):
    yield n - 1
    for i in range(n - 1, 0, -1):
        yield i
        yield i
    yield 1


def directions(di=0, dj=1):
    while True:
        yield di, dj
        di, dj = dj, -di


def matrix(n=4, ival=count(1), fdir=directions, fdist=distances, i=0, j=0):
    m = [[0] * n for i in range(n)]
    for (di, dj), distance in zip(fdir(), fdist(n)):
        for step in range(distance):
            m[i][j] = next(ival)
            i += di
            j += dj
    return m


for rows in matrix():
    print(*map('{:2d}'.format, rows))





#Задача 5: Спиральная матрица дизайна 🔥🔥
#Описание:

#В дизайн студии Романа каждый новый проект получает уникальный номер. 
#Роман хочет отобразить номера текущих проектов в виде квадратной спиральной матрицы по часовой стрелке, начиная с верхнего левого угла. 
#Создайте программу, которая генерирует такую матрицу для заданного числа проектов. Вводится ширина матрицы!

#Таблица входных и выходных данных:

#| Входные данные                      |      Выходные данные       |
#| ------------------------------      | -------------------------  |
#| 3                                   | Матрица проектов:          |
#|                                     | 1 2 3                      |
#|                                     | 8 9 4                      |
#|                                     | 7 6 5                      |
#| 4                                   | Матрица проектов:          | 
#|                                     | 1    2   3 4               |
#|                                     | 12 13 14 5                 |
#|                                     | 11 16 15 6                 |
#|                                     | 10  9  8  7                |