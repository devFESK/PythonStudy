import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import requests
import json
from Data import API_Key

city = "Seoul"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key.apiKey}"

result = requests.get(api)
print(result.text)
data = json.loads(result.text)
print("\njson 데이터 변환 후")
print(data)