from pprint import pprint
import json
import requests

#Задание1
# url = "https://akabab.github.io/superhero-api/api/all.json"
# response = requests.get(url)
# list_hero = ["Hulk", "Captain America", "Thanos"]
# dict_herous = {}
# for dict_hero in response.json():
#     if dict_hero['name'] in list_hero:
#         dict_herous[dict_hero["name"]] = dict_hero['powerstats']['intelligence']
#         max_values = max(dict_herous)
#
# print(f'Самый умный из супергероев {max_values}')

#Задание2
class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, path_to_file, filename):
        href = self._get_upload_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



path_to_file = input('Введите путь до файла')
token = input('Введите токен')
uploader = YaUploader(token)
result = uploader.upload_file_to_disk(path_to_file, 'hfile_name.png')
