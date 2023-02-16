# Serializar
import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinonez",
    "edad": 24
}

# Serializar a un json
objeto_json = json.dumps(persona, indent=2)
# CRear el archivo y guardar la informacion
with open("json/persona.json", "w") as archivo_json:
    archivo_json.write(objeto_json)
# Otra manera
'''
# utilizar la libreria dump que sirve para escribir el archivo sin serializarlo
with open("json/persona.json", "w") as archivo_json:
    json.dump(persona, archivo_json)
'''