def is_prime(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)

# проверка на составное число
        j = 0
        for i in range(2, result-1):
            if result % i == 0:
                j = j +1
        if j <= 0:
            print('Простое')
        else:
            print('Составное')

        return result
    return wrapper

@is_prime
def sum_three(num1,num2,num3):
    return num1+num2+num3

result = sum_three(2, 3, 6)
print(result)
