import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/posts/1"

respuesta = requests.get(url)
data = respuesta.json()
data["title"]
titulo1 = data["title"]
print(titulo1)

url2 = "https://jsonplaceholder.typicode.com/posts/"
respuesta2 = requests.get(url2)
data2 = respuesta2.json()
print(data2)

usuarios = []

for post in data2:
    usuarios.append(post["userId"])
print(usuarios)

miSerie = pd.Series(usuarios)
print(miSerie)

plt.boxplot(usuarios)
plt.show()