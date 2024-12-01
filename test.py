class User:
    def __init__(self,nickname,password,age):
        self.age=age
        self.nickname=nickname
        self.password=hash(password)
        print(password)
        print(hash(password))
        print(hash(password))
        print(hash(password))
        print(hash(password))



user_vasy=User("VASY","сапог",15)
