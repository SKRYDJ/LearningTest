'''
3. Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.
'''

import requests

url = 'https://moex.com'
url_log_text = 'task04\\request_result_getMoexCom.txt'

def get_epam ():
    response = requests.get(url.title())
    with open(url_log_text, 'wb') as f:
        f.write(response.content)
        f.close()
    return f

print(get_epam())