import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/posts/a"

respuesta = requests.get(url)

print(respuesta.status_code)

if respuesta.status_code == 200:
    data = respuesta.json()
    print(data)
else:
    print(f"Error {respuesta.status_code}: no disponemos de esa información")
    