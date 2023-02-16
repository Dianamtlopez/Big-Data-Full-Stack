# Deserializar
import json

# Abrir el archivo
with open("json/persona.json", "r") as archivo_json:
    # deserializar y almacenar datos del json
    datos_json = json.load(archivo_json)
    
    print(type(datos_json))
    print(datos_json)
    print(datos_json["nombre"])