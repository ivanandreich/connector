import requests
import json
import pathlib
from pathlib import Path

url = 'https://api.discogs.com/releases/'
# for release_id in range(1, 10):
#  res = requests.get(url + release_id)


release_id = "200"
res = requests.get(url + release_id)
# path = Path("C", "Users", "63516", "Desktop", "DiscogsJSON", "File")
# print(res.json())
dir_path = pathlib.Path.cwd()
# print(dir_path)

path = Path(dir_path, 'venv', 'Scripts', 'files', 'File.json')

# print(path)

with open(path, 'w') as write_file:
    json.dump(res.json(), write_file)


