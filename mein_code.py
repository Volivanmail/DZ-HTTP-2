from pprint import pprint

import requests

with open('file.txt', encoding='utf-8') as f:
    token = f.read()

class YaUploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }

    def _get_upload_link(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": self.file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self):
        href = self._get_upload_link(file_path=self.file_path).get("href", "")
        r = requests.put(href, data=open(self.file_path, 'rb'))
        pprint(r.json())
        if r.status_code == 200:
            pprint("Success")
        else:
            pprint(f'Ошибка {r.status_code}')

if __name__ == '__main__':
    uploader = YaUploader('Zima.jpg')
    result = uploader.upload()


