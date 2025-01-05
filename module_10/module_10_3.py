from random import randint
import threading
import time

from setuptools.command.build_ext import if_dl


class Bank(threading.Thread):
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            rand = randint(50, 400)
            self.balance += rand
            print(f"\u001b[0;32mПополнение: {rand}. Баланс: {self.balance}.\u001b[0m")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)



    def take(self):
        for i in range(100):
            rand = randint(50, 500)
            print(f"Запрос на {rand}")
            if rand <= self.balance:
                self.balance -= rand
                print(f"Снятие:{rand}. Баланс: {self.balance}")
            else:
                print(f"\u001b[0;31mЗапрос отклонён, недостаточно средств  \u001b[0m")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.take, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
# th2.start()
th1.join()
# th2.join()
print(f'Итоговый баланс: {bk.balance}')