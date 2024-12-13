import  os
import  time
directory=r"."
os.chdir(directory)

for  root, dirs, files in os.walk(directory):
    for file in files:

        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(filepath)
        filesize =os.path.getsize(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir=os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

