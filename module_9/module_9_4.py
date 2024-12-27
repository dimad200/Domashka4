# 1
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
a= list(map(lambda x,y:  list(x).pop(0)==list(y).pop(0), first, second))
print (a)

# 2
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding="utf-8") as file:
            for data in data_set:
                file.write(str(data)+"\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3

class MysticBall():
    def __init__(self,*words):
        self.words=words


    def __call__(self):
        self.word=choice(self.words)
        return self.word

    def __str__(self):
        return self.__call__()

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())



