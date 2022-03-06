import wget

if __name__ == '__main__':
    # 7.2
    # Создаем переменную для хранения ссылки на картинку
    url = 'https://m.dom-eda.com/uploads/images/catalog/item/dfc9a3e974/3cbf3bd41c_1000.jpg'
    # Обращаемся к модулю wget и вызываем метод download()
    # Метод download() скачивает файл по ссылке и возвращает имя скачанного файла
    filename = wget.download(url)