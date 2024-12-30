# Домашнее задание по теме "Генераторы"

# Напишите функцию-генератор all_variants(text).
def all_variants(text):
    # Опишите логику работы внутри функции all_variants.

    # f длина выборки
    for f in range(len(text)):
        for s1 in range(len(text)):
            if s1 + f + 1 > len(text):
                break

            yield (text[s1:s1 + f + 1])


# Вызовите функцию all_variants и выполните итерации.
a = all_variants("abc")
for i in a:
    print(i)
