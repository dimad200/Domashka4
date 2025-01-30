import tkinter, os
from pprint import pprint
from urllib.parse import urlparse
import requests
import xml.etree.ElementTree as ET
# from tkinter import *

window = tkinter.Tk()
window.title('прога для удобства')
window.geometry("500x450")
window.attributes('-topmost', True)
window.grid_columnconfigure(0,minsize=0)
window.grid_columnconfigure(1,minsize=350,pad=5)




def get_xml_click():
    print("Папка",folder_get.get())
    print("файл", entry1.get())

    entry1_1 = entry1.get().replace(".","")

    entry1_1 = entry1_1.replace('"', '')
    print(entry1_1)




    try:
        os.chdir(folder_get.get())
        response = requests.get(url_get_.get())
        print()
        with open(entry1_1+".xml", "wb") as f:
            f.write(response.content)


    except:
        print("Где-то Ошибка!")
    xml_get.delete(0,len(xml_get.get()))
    xml_get.insert(0, entry1_1+".xml")
    xml_folder_get.delete(0,len(xml_folder_get.get()))
    xml_folder_get.insert(0,folder_get.get())

    entry1.delete(0,len(entry1.get()))
    url_get_.delete(0,len(url_get_.get()))

def dowenload(file_name):
    # os.chdir(folder_get.get())
    curent_dir=os.path.split(file_name)[0]
    curent_file=os.path.split(file_name)[1]
    curent_file=curent_file.split(".")[0]
    print(curent_dir,"+", curent_file)
    # print(os.path.split(file_name)[0])
    files_name=os.path.basename(file_name)
    print(files_name, type(files_name))
    try:
        os.chdir(curent_dir)

    except:
        print(os.curdir)


    print(os.getcwd())
    with open(curent_file+".xml_links.txt", "r", encoding="utf-8") as file:
        sufix = 0
        while True:
            # считываем строку
            url = file.readline()
            # print("URL", url)
            if not url:
                break
            response = requests.get(url)

            # получим имя файла

            url = url.split("?")[0]
            # print("URL",url)

            a = urlparse(url)
            # print(a.path)  # Output: /kyle/09-09-201315-47-571378756077.jpg
            # print(os.path.basename(a.path))
            video_name=os.path.basename(a.path)
            if video_name.endswith("audio_0.mp4"):

                video_name=curent_file+".mp3"
                print(video_name)

            elif video_name.endswith(".mp4"):
                sufix+=1
                # print(sufix)
                # video_name=curent_file+"_"+str(sufix)+".mp4"
                video_name=curent_file+".mp4"
                print(video_name)

            with open(video_name, "ab") as f:
                f.write(response.content)


def xml_analiz():
    # print(xml_folder_get.get())
    try:
        ch_dir=xml_folder_get.get()
        os.chdir(ch_dir)
    except:
        print("директория не указана!")

    try:
        os.path.split(xml_get.get())
        if os.path.split(xml_get.get())[0]=="":
            print("директория не найдена. используется из поля 'Папка для анализа'")
            curent_dir = ch_dir
        else:
            curent_dir=os.path.split(xml_get.get())[0]

        file=os.path.split(xml_get.get())[1]
        os.chdir(curent_dir)

        root_node = ET.parse(file).getroot()

        print(root_node)
        print(root_node.attrib)
        video={}
        for i in range(len(root_node[0])):
            if root_node[0][i].attrib["mimeType"]=="video/mp4":
                video["width"]= root_node[0][i].attrib["maxWidth"]
                video["height"]= root_node[0][i].attrib["maxHeight"]
                video["livel_1"]=i

            if root_node[0][i].attrib["mimeType"] == "audio/mp4":
                video["audio/mp4"]= i

            print(video)



            print()

    except:
        print("что то не так!")

    for i in range(len(root_node[0][video["livel_1"]])):

        if root_node[0][video["livel_1"]][i].attrib["width"] == video["width"] and root_node[0][video["livel_1"]][i].attrib["height"] == video["height"]:
            video["livel_2"]=i
            print("TUT       TUT")

    node=root_node[0][video["livel_1"]][video["livel_2"]]
    node_audio = root_node[0][video["audio/mp4"]]
    print(node_audio[1][0].tag, node_audio[1][0].attrib)
    print("metka ya tut ")
    video["audio/BaseURL"]=node_audio[1][0].text
    print(video)
    video["BaseURL"]=node[0].text


    # получение сегменотв видио


    c = []

    temp_len = len(node[1])
    print(temp_len)
    for i in range(1, temp_len):
        if len(c) == 0:
            c.append(node[1][i].attrib["media"])
        else:
            if c[-1] != node[1][i].attrib["media"]:
                c.append(node[1][i].attrib["media"])
    print(c)
    print("GJHGKUJNTUIOtbniuoyildfuytmgbvitgpytfjk!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    c_1=[]
    for i in c:
        print("i=",i)
        if len(c_1) == 0:
            c_1.append(i.split("?")[0])
        else:
            if c_1[-1] != i.split("?")[0]:
                c_1.append(i.split("?")[0])
    print(c_1)



    video['media'] = c_1

    pprint(video)

    # получение готовых ссылок
    print(xml_get.get())
    file_name=xml_get.get()+"_links.txt"
    print(file_name)
    with open( file_name, "w", encoding="utf-8") as file:
        file.write(video["audio/BaseURL"]+"\n")
        for i in video["media"]:
            file.write(video['BaseURL']+i+"\n")



# оформление интерфейса

text = tkinter.Label(window, text='имя для файла ')
text.grid(column=1, row=1)

entry1 = tkinter.Entry(window)
# entry1.place(x=0, y=20,  height=20, width=200)
entry1.grid(column=1, row=2,sticky='ew')

url_get_text = tkinter.Label(window, text='адрес файла ')
url_get_text.grid(column=1, row=3)

url_get_ = tkinter.Entry(window)
url_get_.grid(column=1, row=4,sticky='ew')

folder_text = tkinter.Label(window, text='папка результата')
folder_text.grid(column=1, row=5)

folder_get = tkinter.Entry(window)
folder_get.grid(column=1, row=6,sticky='ew')

button = tkinter.Button(window, text="Получить", command=get_xml_click )
button.grid(column=3, row=3)

xml_for_analiz_folrer= tkinter.Label(window, text='папка для анализа')
xml_for_analiz_folrer.grid(column=1, row=7)

xml_folder_get = tkinter.Entry(window)
xml_folder_get.grid(column=1, row=8,sticky='ew')

xml_for_analiz= tkinter.Label(window, text='файл для анализа')
xml_for_analiz.grid(column=1, row=9)

xml_get = tkinter.Entry(window)
xml_get.grid(column=1, row=10,sticky='ew')
# xml_get.config(width=200, height=5)
# вставка начальных данных
xml_get.insert(0, r"D:\IT\купс\1\Введение Строки байты и кодировки.xml")

button_2 = tkinter.Button(window, text="Проанализировать", command=xml_analiz )
button_2.grid(column=3, row=7)

button_2 = tkinter.Button(window, text="Скачать", command=lambda: dowenload(xml_get.get()),)
button_2.grid(column=3, row=8)



def on_button_click():
    pass





window.mainloop()
