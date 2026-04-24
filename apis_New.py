import requests
import pandas as pd
from IPython.display import Image, display

url = "https://api.nasa.gov/planetary/apod"
api_key = "PphwRDM8QfevwvwevpBllo9T5IdkXLgnkZEWqTwLSiqrxin"

params = {
    "api_key": api_key,
    "date": "2002-08-25"
}

respuesta = requests.get(url, params=params)
data = respuesta.json()
print(data)

display(Image(url=data['url']))

url = "https://api.nasa.gov/DONKI/IPS?"

def obtener_donki(fecha_inicio, fecha_fin):
    params = {
        "api_key": api_key,
        "startDate": fecha_inicio,
        "endDate": fecha_fin
    }
    respuesta = requests.get(url, params=params)
    data = respuesta.json()
    return pd.DataFrame(data)

df = obtener_donki("2023-12-01", "2023-12-31")
print(df)