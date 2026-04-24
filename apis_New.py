import requests

ciudad = 'madrid'

api_key = "eqwe87w1981wew98we89fwe"

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

respuesta = requests.get(url)

data = respuesta.json()

print(type(data))

print(data)