# Задача:использование сторонних библиотек в Python и применение их в различных задачах.
import requests
from bs4 import BeautifulSoup
# import pandas
# import matplotlib.pyplot as plt
from pprint import pprint

URL = 'https://arhivpogodi.ru/arhiv/izhevsk/lastmonth'
r = requests.get(URL)
json_flag = False
print(r)
if r.ok:
    try:
        r = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Содержимое ответа не в формате json.', 'От источника был получен следующий ответ:',
              r, sep='\n')
    else:
        json_flag = True
src = r.text
print(r.encoding)

print(type(src))
# with open("pogoda.html", "w",encoding="utf-8") as file:
#     file.write(src)
#
# инициализируем html-код страницы
soup = BeautifulSoup(src, 'lxml')
# считываем заголовок страницы
title = soup.title.string
print(title)
print(soup)
soup=str(soup)
# Программа выведет: Курсы - Блог компании Селектел

with open("pogoda.html", "w",encoding="utf-8") as file:
    file.write(soup)