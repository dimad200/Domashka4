class Figure:
    sides_count = 0
    __sides = []
    __color = [0, 0, 0]  # (список цветов в формате RGB)
    filled = False

    def get_color(self):
        print(self.__color)

    def __is_valid_color(self, r, g, b):
        if type(r) == int and type(g) == int and type(b) == int:
            if r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255:
                return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for i in range(len(args)):
            if type(args[i]) == int and args[i] > 0:
                return True
        return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.__sides:
            self.__sides=new_sides

#должен возвращать периметр фигуры.
    def __len__(self):
        sum_=0
        for i in range(len(self.__sides)):
            sum_+=self.__sides[1]
        return sum_


sas = Figure()
sas.set_color(1, 20, 3)
sas.get_color()
sas.set_color(1, 90, 3)
sas.get_color()
print(sas.get_sides())
