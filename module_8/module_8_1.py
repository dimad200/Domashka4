def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        a = str(a)
        b = str(b)
    finally:
        result = a + b
        return result


# Проверка
print(add_everything_up(123.456, 'строка'))

print(add_everything_up('яблоко', 4215))

print(add_everything_up(123.456, 7))
