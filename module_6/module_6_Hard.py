import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return (self.__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        # проверяю что число переданных сторон соответствует числу сторон у класса
        if len(sides) == self.sides_count:
            # проверяю что переданные значения сторон целые и положительные
            return all(isinstance(s, int) and s > 0 for s in sides)
        else:
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):

        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__(color, side)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        math.pi * self.__radius ** 2
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):

        side = list([side] * self.sides_count)
        super().__init__(color, *side)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

# По честному, надо бы для куба сделать проверку, что все передаваемые стороны равны между собой.
# Иначе это не куб. И при выполнении кода: cube1.set_sides(1,2,3,4,5,6,7,8,9,10,11,12) стороны не изменятся.
# Но этого нет в задании. :)


# Тесты
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())




# еще проверка для треугольника
# tri = Triangle((12, 34, 56), 2, 2, 7)
# print(tri.get_color())
# print(tri.get_sides())
# tri.set_sides(1, 2, 3)
# print(tri.get_sides())

# cube1.set_sides(1,2,3,4,5,6,7,8,9,10,11,12)
# print(cube1.get_sides())
