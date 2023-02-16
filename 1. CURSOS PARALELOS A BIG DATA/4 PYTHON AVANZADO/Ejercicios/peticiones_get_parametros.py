# Peticiones GET con API de GitHub
import requests

# Enviamos url o endpoint del cual queremos informacion
response = requests.get(
    "https://api.github.com/search/repositories",
    # llaves son parametros de busqueda y valores son los parametros que vamos a usar para la busqueda
    # q: Query, que nos permite hacer consultas y python es el parametro a buscar
    # busca en nombre, descripcion o readme
    params = {"q": "python"}
)
print(response.status_code)

# Almacenamos los datos en una variable llamada data, donde vamos a almacenar el json de la respuesta
data = response.json()
# Podemos imprimir las llaves que generamos en el diccionario a traves de la respuesta
print(data.keys())
print(data['total_count'])