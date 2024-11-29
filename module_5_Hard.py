class User:
    def __init__(self,nickname,password,age):
        self.age=age
        self.nickname=nickname
        self.password=password

class Video:
    def __init__(self, title, duration ,time_now=0, adult_mode=False):
        self.title=title
        self.duration=duration
        self.time_now=time_now
        self.adult_mode=adult_mode
class  UrTube:
    def __init__(self,users,videos,current_user):
        self.users
