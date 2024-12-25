first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(a[0]) - len(a[1]) for a in list(zip(first, second)) if len(a[0]) != len(a[1]))

second_result = (len(first[a]) == len(second[a]) for a in range(len(first)) if len(first) == len(second))

# Проверка
print(list(first_result))
print(list(second_result))
