import sys
# Начало прогрпммы
class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message=message


class  IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message=message



class Car():
    def __init__(self,model,vin_number,number ):
        self.model=str(model)
        if self.__is_valid_numbers(number):
            self.__numbers =number
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number

    def __is_valid_vin(self,vin):
        if not isinstance(vin,int):
            raise IncorrectVinNumber(message='Некорректный тип vin номер')
        if not 1000000 <=vin<= 9999999:
            raise IncorrectVinNumber(message='Неверный диапазон для vin номера')
        return True

    def  __is_valid_numbers(self, number):
        if not isinstance(number,str):
            raise IncorrectCarNumbers(message='Некорректный тип данных для номеров')
        if not len(number)==6:
            raise IncorrectCarNumbers(message='Неверная длина номера')
        return True


# Для проаерки
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message, file=sys.stderr)
except IncorrectCarNumbers as exc:
  print(exc.message, file=sys.stderr)
else:
  print(f'{first.model} успешно создан')


try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message, file=sys.stderr)
except IncorrectCarNumbers as exc:
    print(exc.message, file=sys.stderr)
else:
  print(f'{second.model} успешно создан')



try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message, file=sys.stderr)
except IncorrectCarNumbers as exc:
    print(exc.message, file=sys.stderr)
else:
  print(f'{third.model} успешно создан')