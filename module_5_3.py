# Необходимо дополнить класс House следующими специальными методами:
#
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
#

class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors




    def __str__(self):
        return str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def go_to(self,new_floor):
        # проверяю что значение new_floor не выходит за условия задачи
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for i in (range(1, new_floor + 1)):
                print(i)
        else:
            print("Такого этажа не существует")

# Добавление новых методов
    def __eq__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return False
        # тут False так как проверка на равенство
        # если тип данных другой значит не ровны вернуть False

    def __lt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other,House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other,House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other,House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return True
            # тут True так как проверка на неравенство
            # если тип данных другой значит не ровны вернуть True

    def __add__(self, other):
        if isinstance(other,House):
            self.number_of_floors =self.number_of_floors + other.number_of_floors

            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other

            return self
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other,House):
            self.number_of_floors += other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            return NotImplemented

    def __radd__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self



# class MyClass:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return MyClass(self.value + other.value)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print("11111")
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__


