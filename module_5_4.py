# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):

        cls.houses_history.append(args[0])
        return object.__new__(cls)


    # def __new__(cls, *args, **kwargs):

    def __init__(self,name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors
        # self.houses_history.append(self.name)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __len__(self):
        return self.number_of_floors




    def __str__(self):
        return str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def go_to(self,new_floor):
        # проверяю что значение new_floor не выходит за условия задачи
        if  new_floor < 0 or new_floor > self.number_of_floors :
            print("Такого этажа не существует")
        else:
            for i in (range(1,new_floor+1)):
                print(i)

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



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)