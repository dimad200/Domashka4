import threading
from random import randint
from time import sleep
from queue import Queue



class Table():
    def __init__(self,number):
        self.number=number
        self.guest =None

class Guest(threading.Thread):
    def __init__(self,name: str):
        # super().__init__(self)
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        sleep(randint(3, 10))



class Cafe():
    def __init__(self,*tables):
        for i in tables:
            self.tables=tables
            self.queue=Queue()

    def guest_arrival(self,*guests):
        # guests=list(guests)

        for guest_ in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest=guest_
                    # запускаю поток гостя
                    table.guest.start()
                    print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest_)
                print(f"{guest_.name} в очереди")

#функция для проверки что все столы пусты
    def all_tables_empty(self):
        a=0
        for table in self.tables:
            b=0 if table.guest==None else 1
            a+=b
            result=True if a==0 else False
        return result


    def discuss_guests(self):

        while not self.queue.empty() or not self.all_tables_empty() :
            for table in self.tables:
                if table.guest != None and not table.guest.is_alive():
                    print(f"\u001b[0;32m{table.guest.name} покушал(-а) и ушёл(ушла) \u001b[0m" )
                    print(f"Стол номер {table.number} свободен")
                    table.guest=None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


        # print(f"\u001b[0;31mКОНЕЦ\u001b[0m")


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()