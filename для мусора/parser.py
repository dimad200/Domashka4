# импортируем модуль
from bs4 import BeautifulSoup
import requests
st_accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" # говорим веб-серверу,
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36"
st_cookie="csrftoken=LXV4LbjrbtvpD4NdG9Qb54MhKusjTKk5"
# url="https://urban-university.pro/student/course/5"
url="https://urban-university.pro/"
authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2Njk3ODQwLCJpYXQiOjE3MzYxNDc5MzcsImp0aSI6Ijg1OGI3YTM3YTU1ODQ4NjM5NmZkY2FjZjliNjM5N2I0IiwidXNlcl9pZCI6MzU2OCwidXNlcm5hbWUiOiJkaW1hZEB1ZG0ucnUifQ.PU8AoHweYMJ3QjevL3xwJdipSjeZtHS2JKVP3-EuRQzMDLxaJy-09PyJ7EskrWO4flar4_f9veUXzAyN89R-dA"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent,
   "Cookie":st_cookie
   # "Authorization":authorization
   }


# отправляем запрос с заголовками по нужному адресу
req = requests.get(url, headers)
# считываем текст HTML-документа
src = req.text

# инициализируем html-код страницы
soup = BeautifulSoup(src, "lxml")
# считываем заголовок страницы
# title = soup.title.string
# print(title)
print(src)