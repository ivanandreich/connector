import requests
import json
import pathlib
import time
from pathlib import Path

url = 'https://api.discogs.com/releases/'
headers = {'user-agent': 'ConnectorForBigDataScienceStudyingProject/0.1 +https://github.com/ivanandreich/connector'}
num = 100  # количество файлов
dir_path = pathlib.Path.cwd()

for release_id in range(1, num + 1):
    res = requests.get(url + str(release_id), headers = headers)  # запрос с уникальным юзер-агентом
    r = res.headers
    # сохранение файла в директории C:\Users\63516\PycharmProjects\connector\venv\Scripts\files
    path = Path(dir_path, 'venv', 'Scripts', 'files', str(release_id) + '.json')
    with open(path, 'w') as write_file:
        json.dump(res.json(), write_file)
    time.sleep(3)
# release_id = "200"
# res = requests.get(url + release_id)
# path = Path("C", "Users", "63516", "Desktop", "DiscogsJSON", "File")
# print(res.json())

# print(dir_path)






