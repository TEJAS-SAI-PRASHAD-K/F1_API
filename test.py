from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

response = urlopen('https://api.openf1.org/v1/car_data?driver_number=44&session_key=latest')
data = json.loads(response.read().decode('utf-8'))
soup = BeautifulSoup(response.text, features="xml")
print(soup)