import os

os.chdir(r"D:\IT\купс\Модуль 8. Исключения")
with open("1080p.mp4", "rb") as file1:
    binary_data1 = file1.read()
    with open("1080p (2).mp4", "rb") as file2:
        binary_data2 = file2.read()
        with open("final.mp4", "ab") as file3:
            file3.write(binary_data1)
            file3.write(binary_data2)

