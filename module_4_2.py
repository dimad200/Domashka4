def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()



test_function()
# inner_function()
# Вызов функции inner_function() приводит к ошибке. Она находится вне зоны видимости.
# Её можно вызвать только внутри функции  test_function()

#inner_function()
