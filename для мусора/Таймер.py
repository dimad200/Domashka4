import tkinter
from time import sleep
from tkinter import messagebox
import pystray
from pystray import MenuItem as item
import os
import sys
from PIL import Image
import threading

global vremya
global tik_tak_start
vremya=0
tik_tak_start=0


window = tkinter.Tk()
window.title('Бесплатный таймер')
window.geometry()
text = tkinter.Label(window, text='Бесплатный таймер подаст сигнал через заданное время', background='silver')
text.grid(column=1, row=1)

#
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

ico_path = os.path.join(base_path, "mouse.ico")
mouse_sound_path = os.path.join(base_path, "mouse.mp3")



def quit_window(icon, item):
    icon.stop()
    window.destroy()

def show_window(icon, item):
    icon.stop()
    window.after(0,window.deiconify)

def withdraw_window():
    window.withdraw()
    ico_path = os.path.join(base_path, "alarm.ico")
    image = Image.open(ico_path)
    menu = (item('Выйти', quit_window), item('Развернуть', show_window))
    icon = pystray.Icon("name", image, "Бесплатный таймер", menu)

    icon.run()

# Создаем метку
label = tkinter.Label(window, text="Нажми кнопку", font=("Arial", 14))
label.grid(column=1, row=12)

def on_button_click():
    global tik_tak_start

    global vremya
    try:
        num1 = int(entry1.get())
    except:
        num1=0
    try:
        num2 = int(entry2.get())
    except:
        num2=0
    label.config(text=f"таймер на {num1}минут, {num2}секнд!")
    vremya=num1*60+num2
    # tik_tak(vremya)
    tik_tak_start=1
    # threading.Thread(target=tik_tak,args=(vremya,)).start()

def tik_tak():
    global tik_tak_start
    global vremya
    pusk=1
    while pusk:
        print(tik_tak_start, vremya, pusk)

        while vremya > 0 and tik_tak_start!=0:
            vremya -= 1
            vremya_label.config(text=f"Осталось: {vremya}")
            print(vremya)
            sleep(1)
            window.update()
            if (vremya == 0):
                tkinter.messagebox.showinfo("Время вышло!", "Время вышло!")
                tik_tak_start=0
                pusk=0
                print(tik_tak_start, vremya, pusk)


button = tkinter.Button(window, text="Старт", command=on_button_click)
button.grid(column=1, row=13)


text_min = tkinter.Label(window, text='Минуты:')
text_sec = tkinter.Label(window, text='Секунды:')
text_min.grid(column=1, row=2)
text_sec.grid(column=2, row=2)

entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)
entry1.grid(column=1, row=3)
entry2.grid(column=2, row=3)

vremya_label = tkinter.Label(window, text=f"осталось: {vremya}", font=("Arial", 14))
vremya_label.grid(column=1, row=5)
threading.Thread(target=tik_tak,args=()).start()
window.protocol('WM_DELETE_WINDOW', withdraw_window)
window.mainloop()

