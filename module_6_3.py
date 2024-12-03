class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz)
        self._cords[0] = self._cords[0] + dx * self.speed
        self._cords[1] = self._cords[1] + dy * self.speed
        self._cords[2] = self._cords[1] + dz * self.speed



a1 = Animal(10)
print(a1._cords)
a1._cords = [10, 10, 10]
print(a1._cords)
