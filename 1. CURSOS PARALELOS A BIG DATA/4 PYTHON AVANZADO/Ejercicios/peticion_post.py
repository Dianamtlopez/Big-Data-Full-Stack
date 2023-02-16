import requests

url = "https://webhook.site/91c598c1-9e63-4ea5-83fd-914a2048e974"
# Vamos a en esta peticion post, vamos a enviar datos relacionados a orden de comida
# vamos asimular que nuestro endpoint es un restaurante y que el endpont va a recibirla
# los datos que enviamos son el cuerpo de la peticion, para construri el cuerpo, debemos
# dar el formato de json, pero desdepython se escribe en diccionario ya que es la estructura
# de datos que se asemeja y puede ser convertida a un json
# creamos una variable de carga asignandole un diccionario
payload = {"plato": "pasta", "cantidad": 2}
# Creamos una variable, enviamos en forma de diccionario el nombre de la persona que hizo la orden
query_params = {"nombre": "Diana"}
# Creamos nuestra petición, el primer argumento es url o endpoint, luego datos o cuerpo de la
# peticion
response = requests.post(url, data=payload, params=query_params)
# Imprimimos el status_code de la respuesta
print(response.status_code)
# para ver el contenido en formato txto usamos response.text
print(response.text)
