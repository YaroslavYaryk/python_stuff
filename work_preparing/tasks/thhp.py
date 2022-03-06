# 2. Импортируем модуль client из пакета http
# Модуль client позволяет отправлять и обрабатывать HTTP запросы к веб-серверу
from http import client
from pprint import pprint

if __name__ == '__main__':
    # 3.1. Создаем соединение по адресу 'www.google.com'
    # Для этого обращаемся к модулю client
    # И вызываем конструктор класса HTTPConnection()
    connection = client.HTTPConnection('www.google.com')
    # 3.2. Отправляем GET запрос к корневой странице веб-сервера
    connection.request('GET', '/')
    # 3.3. Получаем ответ на наш запрос
    res = connection.getresponse()
    # Из полного ответа достаем интересующую нас веб-страницу(ее HTML код)
    page = res.read()
    pprint(page)
