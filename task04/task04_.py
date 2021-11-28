'''
Все файлы, которые будут создаваться для задач должны начинаться с префикса "task04"
Все файлы отправить на github

1. Создать скрипт, который через параметр запуска получает имя исполняемого файла.
И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не
может быть запущен и т.д.) сделать через исключения.
'''

НЕ ЯСЕН СЦЕНАРИЙ ЗАДАНИЯ

import os
import subprocess

file = os.path.basename('script04_sub.txt')
networkStats = subprocess.call(['notepad', file], stdout=subprocess.PIPE)
try:
    print('Script correct')
except FileNotFoundError:
    print('File does not exist')

'''
2. Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
'''

import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def files_in_cat():
    for root, dirs, files in os.walk("C:\\"):
        return files
print(files_in_cat())
logger.info(f"{len(files_in_cat())} Files")