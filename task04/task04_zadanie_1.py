'''
Все файлы, которые будут создаваться для задач должны начинаться с префикса "task04"
Все файлы отправить на github

1. Создать скрипт, который через параметр запуска получает имя исполняемого файла.
И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не
может быть запущен и т.д.) сделать через исключения.
'''

import subprocess

file = 'task04\\ping.txt'


def open_file(file):
    try:
        subprocess.call(file, shell=True)
    except:
        print('File \"{}\" does not exist'.format(file))


open_file(file)
