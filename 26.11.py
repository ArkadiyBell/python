class Counter:
    def __init__(self, start=0):
        self.value=start
    def inc(self, n = 1):
        self.value+= n
    def dec(self, n=1):
        self.value-= n
        if self.value<0:
            self.value = 0
class NonDecCounter(Counter):
    def dec(self, n = 1):
        pass
class LimitedCounter(Counter):
    def __init__(self, start = 0, limit = 10):
        self.value = start
        self.limit = limit
    def inc(self, n = 1):
        self.value+=n
        self.value = min(self.value, self.limit)
        
counter = Counter()
print(f'Начальное значение: {counter.value}')

counter.inc(5)
print(f'Увеличен на 5: {counter.value}')

counter.dec(7)
print(f'Уменьшен на 7: {counter.value}')

counter.dec(1)
print(f'Попытка уменьшения ниже нуля: {counter.value}')

non_dec_counter = NonDecCounter(start=5)
print(f'Начальное значение: {non_dec_counter.value}')

non_dec_counter.inc(3)
print(f'Увеличен на 3: {non_dec_counter.value}')

non_dec_counter.dec(4)
print('Попытка уменьшения:', non_dec_counter.value)

limited_counter = LimitedCounter(limit=15)
print(f'Начальное значение: {limited_counter.value}')

limited_counter.inc(12)
print(f'Увеличен на 12: {limited_counter.value}')

limited_counter.inc(6)
print('Попытаемся превысить лимит:', limited_counter.value)

limited_counter.dec(9)
print('Уменьшение допустимо:', limited_counter.value)

limited_counter.inc(100)
print("Превышаем лимит:", limited_counter.value)
print("\n")

########################################################################################

class Bachelor:
    def __init__(self, first_name, last_name, group, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark == 5:
            return 10000
        elif self.average_mark > 3:
            return 5000
        else:
            return 0

class Undergraduate(Bachelor):
    def __init__(self, first_name, last_name, group, average_mark, scientific_work=None):
        super().__init__(first_name, last_name, group, average_mark)
        self.scientific_work = scientific_work

    def get_scholarship(self):
        if self.average_mark == 5:
            return 15000
        elif self.average_mark > 3:
            return 7500
        else:
            return 0


students = [
    Bachelor("Турал", "Сулейманов", "14123", 3.5),
    Undergraduate("Анна", "Петрова", "12344", 5, "Исследование квантовых вычислений"),
    Bachelor("Дмитрий", "Горбачев", "14121", 4.6),
    Undergraduate("Екатерина", "Васильева", "15378", 4.8, "Анализ данных")
]


for student in students:
    print(f"{student.first_name} {student.last_name}: {student.get_scholarship()} рублей")
print("\n")
    
########################################################################################
class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value
        
class Buy(Product):
    def __init__(self, name, price, weight, count):
        super().__init__(name, price, weight)
        self.__count = count
        self.__total_price = self.price * self.count
        self.__total_weight = self.weight * self.count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value
        self.__total_price = self.price * self.count
        self.__total_weight = self.weight * self.count

    @property
    def total_price(self):
        return self.__total_price

    @property
    def total_weight(self):
        return self.__total_weight
    
class Check(Buy):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight, quantity)

    def output(self):
        print(f"Название товара: {self.name}")
        print(f"Цена одного товара: {self.price}")
        print(f"Вес одного товара: {self.weight}")
        print(f"Количество товара: {self.count}")
        print(f"Общая стоимость покупки: {self.total_price}")
        print(f"Общий вес покупки: {self.total_weight}")

product = Check("Яблоко", 30, 0.2, 5)
product.output()
print('\n')
########################################################################################
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Parallelepiped(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return f"Параллелепипед с рёбрами: {self.length}, {self.width}, {self.height}"


class Cube(Parallelepiped):
    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length)

    def __str__(self):
        return f"Куб с ребром {self.length}"


class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * pi * self.radius ** 2

    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    def __str__(self):
        return f"Шар с радиусом {self.radius}"


class Cylinder(Shape):
    def __init__(self, base_radius, height):
        self.base_radius = base_radius
        self.height = height

    def surface_area(self):
        lateral_surface_area = 2 * pi * self.base_radius * self.height
        bases_surface_area = 2 * pi * self.base_radius ** 2
        return lateral_surface_area + bases_surface_area

    def volume(self):
        return pi * self.base_radius ** 2 * self.height

    def __str__(self):
        return f"Цилиндр с высотой {self.height} и радиусом основания {self.base_radius}"


class Ellipsoid(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def surface_area(self):
        p = 1.6075
        surface_area = (
            4 * pi *
            (((self.a * self.b) ** p) + ((self.a * self.c) ** p) + ((self.b * self.c) ** p)) ** (1 / p)
        )
        return surface_area

    def volume(self):
        return 4 / 3 * pi * self.a * self.b * self.c

    def __str__(self):
        return f"Эллипсоид с параметрами: {self.a}, {self.b}, {self.c}"


def find_big_shape(shapes):
    sum_volumes = sum(shape.volume() for shape in shapes)

    for shape in shapes:
        if shape.volume() >= sum_volumes / 2:
            print(f"ОбЪём больший или равный суммарному объёму остальных фигур имеет {shape}")



cube = Cube(10)
sphere = Sphere(5)
cylinder = Cylinder(3, 7)
parallelepiped = Parallelepiped(4, 5, 6)
ellipsoid = Ellipsoid(8, 9, 10)


shapes = [cube, sphere, cylinder, parallelepiped, ellipsoid]

find_big_shape(shapes)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

