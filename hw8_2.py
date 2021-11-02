import requests, os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = []
        for root, dirs, files in os.walk(file_path):
            for file in files:
                file_list.append(os.path.join(file))
        for name in file_list:
            fool_path = file_path + '/' + name
            self.upload_file_to_disk(name, fool_path)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:/Users/axata/PycharmProjects/pythonProject/res'
    token = ' '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)