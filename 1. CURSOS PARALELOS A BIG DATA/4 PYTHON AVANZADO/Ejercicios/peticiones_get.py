# Peticiones GET con API de GitHub
import requests

# Enviamos url o endpoint del cual queremos informacion
response = requests.get("https://api.github.com")
# imprimimos la respuesta
print(response)
# si quiesieramos ver los headers hariamos lo siguiente
print(response.headers)
# Para saber el código de estado de la respuesta
print(response.status_code)
# Para acceder a las respuestas, lo podemos hacer de tres maneras
# Content retorna la respuesta en bytes y en forma de diccionario
# Se identifica porque el primer caracter de la respuesta es una b
print(response.content)
# Text retorna la respuesta de tipo string
print(response.text)
# La funcion json arroja una respuesta en forma de diccionario
print(response.json())
# Convierte esta respuesta en un diccionario en python, al que podemos
# acceder a sus valores llamandolo entre corchetes y comillas
print(response.json()["current_user_url"])

