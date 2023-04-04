#Задание2
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Определяем запрос для получения ссылки согласно документации Yandex.API
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        # Выделяем имя загружаемого файла
        filename = file_path.split('/', )[-1]
        # Определяем формат заголовков запроса
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        # Определяем параметры запроса (назначаем путь загрузки, имя файла и разрешаем перезапись)
        params = {"path": filename, "overwrite": "true"}
        # Выполняем запрос на получение ссылки для загрузки
        _response = requests.get(upload_url, headers=headers, params=params).json()

        # Выделяем ссылку для загрузки в отдельную переменную
        href = _response.get("href", "")
        # Выполняем запрос на загрузку файла на Яндекс.Диск по полученной ссылке
        responce = requests.put(href, data=open(file_path, 'rb'))
        # Получаем статус отправки файла
        responce.raise_for_status()
        # Проверяем успешность отправки по полученному статусу
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"

# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = input('Введите путь к загружаемому файлу')
#     token = input('Введите токен')
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)
#     print(f'Ваш файл {path_to_file} загружается на Яндекс.Диск')
#     print(result)


if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:\Homework\ya_disk\hfile_name.png'
    token = 'y0_AgAAAAAOje4JAADLWwAAAADcWBixenJ3RHOsR8Oo9e2u0QQM4O3n8i4'
    # Определяем экземпляр класса для токена пользователя
    uploader = YaUploader(token)
    # Загружаем файл на диск
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)

# создаём список пустой list = [] и в него через функцию .append() добавляем название файла! потом список распаковываем и загружаем.
    #путь к папке на компьютере C:\Homework\ya_disk
    # путь к файлу https://disk.yandex.ru/d/C5oLongIsnrXkg
    # y0_AgAAAAAOje4JAADLWwAAAADcWBixenJ3RHOsR8Oo9e2u0QQM4O3n8i4
    #имя загружаемого файла C:\Homework\ya_disk\file_name.png
