# Необходимо дополнить класс House следующими специальными методами:
#
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>

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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))

# izba = House("хоромы главы муниципалитета в деревне 'Гадюкино'", 1)
# print(len(izba))
# print(izba)
# print(str(izba))