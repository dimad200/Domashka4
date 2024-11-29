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
    def __init__(self,users,videos,current_user=User):
        self.usersг=users
        self.videos=videos
        self.current_user=current_user

    def log_in(self):
        pass
    def register(self,nickname, password, age):
        pass
    def log_out(self):
        self.current_user=None
    def add(self):
        pass
