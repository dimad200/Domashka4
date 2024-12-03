class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] = self._cords[0] + dx * self.speed
        self._cords[1] = self._cords[1] + dy * self.speed
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = self._cords[2] + dz * self.speed
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")


a1 = Animal(10)
print(a1._cords)
a1._cords = [10, 10, 10]
print(a1._cords)
