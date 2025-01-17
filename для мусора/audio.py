import moviepy as mp
import os
import sys
import pathlib

os.chdir("G:\курс")
work_dir=os.getcwd()  # получить  текущую дерикторию

files_=os.listdir() # получить содержание дирриктории
name="file_list.txt" # файл куда запишем список всех найденных файлов


with open(name, "w", encoding="utf-8") as file:
    for k in os.walk(work_dir):
        for a1_ in k[2]:

            file.write(f"{k[0]}\\{a1_}\n")


file2 = open("Only_mp4_mp3.txt", 'w', encoding="utf-8")
with open(name, "r" ,encoding="utf-8") as file:
    while True:
        # считываем строку
        line = file.readline()
        if line.endswith(".mp4\n")  or line.endswith( ".mp3\n"):
            file2.write(line)
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        # print(line.strip())
file2.close()

with open("Only_mp4_mp3.txt", "r" ,encoding="utf-8") as file:
    mp3=None
    mp4=None
    while True:
        # считываем строку
        line = file.readline()
        if not line:
            break
        if line.endswith(".mp3\n"):
            mp3 =line
            s2 = "\n"
            mp3 = mp3.replace(s2, '')

        elif line.endswith(".mp4\n"):
            s2 = "\n"
            mp4=line
            mp4=mp4.replace(s2, '')

        if not mp3==None and not mp4==None:
            path = pathlib.Path(mp3)
            mp3=path.name
            path = pathlib.Path(mp4)
            mp4=path.name
            os.chdir(path.parent)
            print(mp3)
            print(mp4)
            print(path.parent)

            audio = mp.AudioFileClip(mp3)
            video = mp.VideoFileClip(mp4)
            final_video = video.with_audio(audio)
            s1 = mp3
            s2 = ".mp3"
            s3 = s1.replace(s2, '_final.mp4')
            mp4=None
            mp3=None
            print(s3)
            final_video.write_videofile(s3)




# # Загрузка аудиофайла
#  print((f'{base_path}Audio/file.mp3'))
# print(base_path)
# audio = mp.AudioFileClip('1.mp3')
#
# # Загрузка видеофайла

#
# # Добавление внешнего звука к видео
# final_video = video.with_audio(audio)
#
# # Экспорт итогового видеофайла
# final_video.write_videofile("output_video.mp4")