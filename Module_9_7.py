def is_prime(func):
    def wrapper(*args):
        # print(*args)
        res=func(*args)
        for i in range(2, res):
            # print("i=", i,"res=",res,  "   res % i=", res % i)
            if res % i == 0:
                print ("Составное")
                break
            if i==res-1:
                print("Простое")


        # if res
        return res
    return wrapper

@is_prime
def sum_three(a,b,c):
    sum_=a+b+c
    return sum_



print(sum_three(2,3,6))

