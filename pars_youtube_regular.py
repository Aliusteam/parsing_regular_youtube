# Сбор последних 30 видео Оксаны Мащенко с youtube.com с помощью регулярных выражений
# Канал: https://www.youtube.com/c/ОксанаМащенкоИнвестиции2020/videos 
# Результат: Создаю новый инвестиционный портфель для новой жизни! Какие инвест идеи я буду использовать?"
# https://www.youtube.com/watch?v=WAmLxRERNOQ

import requests
import re

URL = 'https://www.youtube.com/c/%D0%9E%D0%BA%D1%81%D0%B0%D0%BD%D0%B0%D0%9C%D0%B0%D1%89%D0%B5%D0%BD%D0%BA%D0%BE%D0%98%D0%BD%D0%B2%D0%B5%D1%81%D1%82%D0%B8%D1%86%D0%B8%D0%B82020/videos'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://www.youtube.com'

s = requests.get(URL).text

url = []  # Сбор url 
k = r'{"webCommandMetadata":{"url":"/(.+?)"'
w = re.findall(k, s)
for x in w:
  if x[0] == 'w':
    url.append(x)

i = 0
k = r'text":"(.+?)"'   # Сбор Описания
w = re.findall(k, s)
for x in w:
  if x[0] != 'A' :
    if  x[0] != 'N':
      print(x)
      print(HOST+'/'+url[i])
      i += 1
      print()
      if i == 30:
        break







