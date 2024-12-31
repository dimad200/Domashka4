def is_prime(func):
    def new_func(*args):
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
    return new_func

@is_prime
def sum_three(a,b,c):
    sum_=a+b+c
    return sum_



print(sum_three(1,3,3))

