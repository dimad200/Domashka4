from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.age = age
        self.nickname = nickname
        self.password = hash(password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    #
    # def __str__(self):
    #     return str(f"Название: {self.title}")


class UrTube:

    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in range(len(self.users)):
            if nickname in self.users[i].nickname:
                if hash(password) == self.users[i].password:
                    print("Есть такой!")
                    self.current_user=nickname


    def register(self, nickname, password, age):

        if len(self.users)==0:

            a = User(nickname, password, age)
            self.users.append(a)
            self.current_user = a.nickname
        else:
            for i in range(len(self.users)):
                if nickname in self.users[i].nickname:
                    print(f"Пользователь {nickname} уже существует")
                else:

                    a = User(nickname, password, age)
                    self.users.append(a)
                    self.current_user = a.nickname





    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in range(len(args)):
            self.videos.append(args[i])

    def get_videos(self, vidio_search):
        result_search = []
        self.vidio_search = vidio_search.lower()
        for i in range(len(ur.videos)):
            if self.vidio_search in ur.videos[i].title.lower():
                result_search.append(ur.videos[i].title)
        return result_search

    def watch_video(self, watch_video):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")

        else:
            for i in range(len(ur.videos)):
                if watch_video == self.videos[i].title:
                    for k in range(self.videos[i].time_now, self.videos[i].duration):
                        print(range(self.videos[i].time_now, self.videos[i].duration))
                        print("POKAZ")


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
#
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
####
print(ur.current_user)
####

# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
