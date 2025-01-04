import time
import threading
import datetime
from time import sleep

def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):

            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time=datetime.datetime.now()
wite_words(10,"example1.txt")
wite_words(30,"example2.txt")
wite_words(200,"example3.txt")
wite_words(100,"example4.txt")
print(f"Работа потоков: {datetime.datetime.now()-start_time}")

potok_1=threading.Thread(target=wite_words,args=(10,"example5.txt"))
potok_2=threading.Thread(target=wite_words,args=(30,"example6.txt"))
potok_3=threading.Thread(target=wite_words,args=(200,"example7.txt"))
potok_4=threading.Thread(target=wite_words,args=(100,"example8.txt"))
start_time=start_time=datetime.datetime.now()
potok_1.start()
potok_2.start()
potok_3.start()
potok_4.start()
potok_1.join()
potok_2.join()
potok_3.join()
potok_4.join()
print(f"Работа потоков: {datetime.datetime.now()-start_time}")