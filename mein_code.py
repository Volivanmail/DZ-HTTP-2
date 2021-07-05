from pprint import pprint

import requests
with open('file.txt', encoding='utf-8') as f:
    token = f.read()

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}' + token
        }

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/publish"
        headers = self.get_headers()
        r = requests.put(url=url, data=open(self.file_path, 'rb'), headers=headers )
        if r.status_code == 201:
            pprint("Success")
        else:
            pprint(f'Ошибка {r.status_code}')


if __name__ == '__main__':
    uploader = YaUploader('D:\Учеба Pyton\PC cod\DZ HTTP 2\cod.docx')
    result = uploader.upload()
