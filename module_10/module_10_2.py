import  threading
import time
from turtledemo.penrose import start


class Knight(threading.Thread):
    def __init__(self,name: str,power: int):
        threading.Thread.__init__(self)
        self.name=name
        self.power=power


    def run(self):
        enemy = 100
        day=0
        print(f"{self.name}, на нас напали")
        while enemy >0:
            enemy=enemy-self.power
            day+=1
            print(f"{self.name} сражается {day}..., осталось {enemy} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")