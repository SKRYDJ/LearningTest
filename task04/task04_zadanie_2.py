'''
2. Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
'''

import os
import logging

logging.basicConfig(level=logging.DEBUG, filename='task04\\task04_logger_zadanie_2.log', filemode='w')
logger = logging.getLogger(__name__)


def files_in_cat():
    for root, dirs, files in os.walk('task04'):
        return files


logger.debug(files_in_cat())
