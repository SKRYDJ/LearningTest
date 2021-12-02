'''
Работу поместить в файл task05.py и разместить его в репозитории.


1. Работа с HTML
Скачать содержимое страницы https://epam.com с помощью requests
Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4)

2. Базы данных

Работа с sqlite.
С помощью SQL запросов создать таблицу содержаюую 2 стобца: номер и имя
Добавить три строки с данными.
Получить данные из таблицы и распечатать их на экране.

Если есть доступ к сетевым базам данных mysql, postgrsql можно выполнить те же операции с этими базами данных.
'''

# 1 посчитать div

from bs4 import BeautifulSoup
import requests
import sqlite3

url = 'https://moex.com'
response = requests.get(url).text
countDiv = len(BeautifulSoup(response, 'html.parser').find_all('div'))

print(countDiv)


#2 Создать таблицу, два столбца номер и имя, добавить три строки, селектнуть и распечатать на экран


conn = sqlite3.connect(':memory:')
baza = conn.cursor()

baza.execute("CREATE TABLE homework (number INTEGER, name VARCHAR)").\
    execute("INSERT INTO homework VALUES (10, 'Sergey'), (19, 'Mike'), (23, 'Alexander')")

conn.commit()

for row in baza.execute("SELECT * FROM homework"):
    print(row)


