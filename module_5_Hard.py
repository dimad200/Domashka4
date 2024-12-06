from pprint import pprint
from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.age = age
        self.nickname = nickname
        self.password = hash(password)

    def __str__(self):
        return str(f"Никнейм: {self.nickname}")


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return str(f"Название: {self.title}")


class UrTube:

    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in range(len(self.users)):
            if nickname == self.users[i].nickname:
                if hash(password) == self.users[i].password:
                    print("Есть такой!")
                    self.current_user=nickname


    def register(self, nickname, password, age):

        if len(self.users)==0:

            a = User(nickname, password, age)
            self.users.append(a)
            self.current_user = a.nickname
        else:
            user_in_list=False
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    user_in_list=True
            if user_in_list==True:
                print(f"Пользователь {nickname} уже существует")
            else:
                a = User(nickname, password, age)
                self.users.append(User(nickname, password, age))
                self.current_user = a.nickname
                print("Создал нового")
                #
                #     print(f"Пользователь {nickname} уже существует")
                #     break
                # else:
                #     a = User(nickname, password, age)
                #     self.users.append(User(nickname, password, age))
                #     self.current_user = a.nickname





    def log_out(self):
        self.current_user = None

    def add(self, *args):
        # если список видео пуст то просто добавляем
        if len(self.videos)==0:
            for i in range(len(args)):
                self.videos.append(args[i])
        # проверка на наличие:
        else:
            video_in_list = False
            for i in range(len(self.videos)):
                for k in range(len(args)):
                    if self.videos[i]==args[k]:
                        print("такой есть")
                        video_in_list=True

            if video_in_list==False
        else:
            self.videos.append(args[k])


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
            # Инициализация age
            age = 0
            for i in range(len(self.users)):
                if self.users[i].nickname == self.current_user:
                    age = self.users[i].age
            if age <18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")

            else:
                for i in range(len(self.videos)):
                    if watch_video == self.videos[i].title:
                        for k in range(self.videos[i].time_now, self.videos[i].duration):
                            print(k + 1, end=" ")
                            sleep(1)
                        print("Конец видео")
                        self.videos[i].time_now = 0


# # Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
ur.add(v1, v2)
print(ur.videos)
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# #
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ####
# print(ur.current_user)
# ####
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#
# # ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

# ******
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# print(ur.current_user)
# ur.register('vasya_pu', 'lolkekcheburek', 13)
# print(ur.current_user)
# ur.register('vasya_pup', 'lolkekcheburek', 13)
# print(ur.current_user)
# ur.register('bayden_loh', 'lolkekcheburek', 13)
# print(ur.current_user)