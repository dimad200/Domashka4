from itertools import count


def custom_write(file_name, strings):
    file_name =file_name
    strings=strings
    strings_positions= {}

    file = open(file_name, 'a',encoding="utf-8")

    count_strings=0
    for s in strings:
        count_strings+=1
        strings_positions[(count_strings,file.tell())]=s
        file.write(s+"\n")
    file.close()
    return strings_positions
# Проверка
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)