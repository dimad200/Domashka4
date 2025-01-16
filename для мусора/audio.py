import moviepy as mp
import os
import sys

os.chdir('D:\\video\\')
base_path = os.path.abspath(".")
dir="D:/video/"
# Загрузка аудиофайла
print((f'{base_path}Audio/file.mp3'))
print(base_path)
audio = mp.AudioFileClip('1.mp3')

# Загрузка видеофайла
video = mp.VideoFileClip('.1.mp4')

# Добавление внешнего звука к видео
final_video = video.with_audio(audio)

# Экспорт итогового видеофайла
final_video.write_videofile("output_video.mp4")