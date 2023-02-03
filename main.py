import requests
from bs4 import BeautifulSoup
import os
import json
import datetime
import re

result_json_content = {}
result_json_content['timestamp'] = datetime.datetime.now().strftime('%d.%m.%Y')
result_json_content['loipen'] = []

url = 'https://www.bergfex.ch/berneroberland/langlaufen/beatenberg/loipen/'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
bericht = page.find('dl', {'class': 'dl-horizontal dt-large loipen-bericht'})
status = bericht.find('dt', string = 'Betrieb')
status = status.findNext('dd').string
loipe = 'Beatenberg ' + str(status).strip()
result_json_content['loipen'].append({
	'loipe': 'Beatenberg',
    'status': status
	})
# print(loipe)
url = 'https://www.bergfex.ch/berneroberland/langlaufen/jungfrau-region-lauterbrunnen/loipen/'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
bericht = page.find('dl', {'class': 'dl-horizontal dt-large loipen-bericht'})
status = bericht.find('dt', string = 'Betrieb')
status = status.findNext('dd').string
loipe = 'Lauterbrunnen ' + str(status).strip()
result_json_content['loipen'].append({
	'loipe': 'Lauterbrunnen',
    'status': status
	})
# print(loipe)
url = 'https://www.bergfex.ch/berneroberland/langlaufen/jungfrau-region-grindelwald/loipen/'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
bericht = page.find('dl', {'class': 'dl-horizontal dt-large loipen-bericht'})
status = bericht.find('dt', string = 'Betrieb')
status = status.findNext('dd').string
loipe = 'Grindelwald ' + str(status).strip()
result_json_content['loipen'].append({
	'loipe': 'Grindelwald',
    'status': status
	})
# print(loipe)
print(result_json_content)

loipen_json_filename = 'docs/loipen.json'
if os.path.exists(loipen_json_filename):
    os.remove(loipen_json_filename)

with open(loipen_json_filename, 'a') as loipen_json_file:
    json.dump(result_json_content, loipen_json_file)
