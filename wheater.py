import requests

API_KEY = "1857797cca93b55be04b95017110dddb"
BASE_URL = "http://api.open.openweathermap.org/data/2.5/weather"

city = input("enter your city:")

requesr_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
print(requesr_url)

