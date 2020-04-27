#   Hacer peticiones HTTP
import requests

params = {"q": "pizza"}
r = requests.get("http://bing.com", params=params)
print("Status", r.status_code)

print(r.url)

print(r.text)

#   Creamos un archivo y escribimos el contenido de la request
f = open("./page.html", "w+")
f.write(r.text)