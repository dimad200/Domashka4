from pprint import pprint

class Product():
    def __init__(self, name, weight,category):
        self.name = str(name)
        self.weight = float(weight)
        self.category=str(category)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.weight, self.category)


class Shop():

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result_str=file.read()
        file.close()
        return result_str

    def add(self, *products):
        a = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if str(i) in a:
                print(f"Продукт {i.name} уже есть в магазине")
            else:
                file.write(str(i) + "\n")
        file.close()

# Проверка:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())