# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# a= list(map(lambda x,y:  list(x).pop(0)==list(y).pop(0), first, second))
# print (a)
# 2
def get_advanced_writer(file_name):
    print(file_name)
    def write_everything(*data_set):
        with open(file_name, 'w', encoding="utf-8") as file:
            for data in data_set:
                file.write(str(data)+"\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# asa('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Замыкание:
#
# Внутри этой функции, напишите ещё одну - , где *data_set - параметр принимающий неограниченное количество данных любого типа.
#
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
#
# Функция get_advanced_writer возвращает функцию write_everything.
#
#
#
# Данный код:
#
# write = get_advanced_writer('example.txt')
#
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#
# Запишет данные в файл в таком виде:
