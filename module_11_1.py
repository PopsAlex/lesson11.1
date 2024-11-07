import requests as req
import numpy
import PIL
from PIL import Image


class Requests:
    def __init__(self, link):
        self.link = link
        self.response = req.get(self.link)

    def get_ok(self):
        status = self.response.status_code
        if status == 200:
            print('Ответ найден')
        elif status == 404:
            print('Ответ не найден')
        return self.response

    def get_content(self):
        self.response.encoding = 'utf-8'
        content = self.response.text
        return content

    def get_headers(self):
        return self.response.headers

class Numpy:
    def __init__(self, args):
        self.args = args
        self.array = numpy.array(self.args)
        self.a = self.array[1]
        self.b = self.array[0]
        self.c = self.array[2]

    def size(self):
        return f'Размер каждого элемента в байтах: {numpy.array(self.args).itemsize}'

    def index(self):
        print(self.array, '\n')
        return f'В первой строчке третьей колонки находится элемент: {self.array[0, 2]}'

    def type(self):
        return f'Тип данных элементов в массиве: {self.array.dtype}'

    def conc_and_sort(self):
        print('Пример соединения:')
        print(numpy.concatenate((self.a, self.b, self.c)))
        print(numpy.sort(numpy.concatenate((self.a, self.b, self.c))), '\n')
        return numpy.sort(numpy.concatenate((self.a, self.b, self.c))).reshape(3, 3)

    def sum(self):
        print('Пример сложения: ')
        return self.a + self.b + self.c

    def sum1(self):
        print('Пример сложения по осям столбцов: ')
        return self.array.sum(axis=1)

class Pillow:
    def __init__(self, file):
        self.file = file
        self.image = Image.open(self.file)

    def image_open(self):
        with self.image:
            image = self.image.show()
            return f'Изображение {self.file} открыто'

    def size(self):
        with self.image:
            size = self.image.size
            return f'Размер изображения: {size[0]}x{size[1]}'

    def cropped(self):
        with self.image:
            cropped = self.image.crop((0, 30, 736, 522))
            new_file = 'cropped_image.jpeg'
            cropped.save(new_file)
            cropped.show()
            return f'Изображение обрезано: {cropped.size[0]}x{cropped.size[1]}, новое название: {new_file}'

getting = Requests('https://ru.wikipedia.org/wiki/Python')

print('')
print(getting.get_ok())
print('')
print(getting.get_content())
print('')
print(getting.get_headers())
print('')

_numpy = Numpy([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(_numpy.size())
print('')
print(_numpy.index())
print('')
print(_numpy.type())
print('')
print(_numpy.conc_and_sort())
print('')
print(_numpy.sum())
print('')
print(_numpy.sum1())
print('')

depict = Pillow('image.jpeg')

print(depict.image_open())
print('')
print(depict.size())
print('')
print(depict.cropped())

