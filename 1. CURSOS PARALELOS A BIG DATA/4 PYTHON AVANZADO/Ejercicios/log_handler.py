import logging
logger = logging.getLogger(__name__)
# Cuando usamos handlers, ya no podemos usar la libreria basicConfig de la libreria logging, debemos
# definir nivel y formato a traves del logger o la clase del handler que vamos a usar
logger.setLevel(logging.DEBUG)
# Crear controlador para la consola
handler_consola = logging.StreamHandler()
# Definir el formato
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s ")
# para añadir el formato creado a la funcion, se usa setFormatter
handler_consola.setFormatter(formato_logs)
# Definir el logger al cual pertenece el controlador creado
logger.addHandler(handler_consola)
# para escribir los logs en un archivo
handler_archivo = logging.FileHandler("archivo.log")
# Definimos el nivel mínimo del handler es decir el nivel minimo para que un archivo se guarde
# En el archivo creado
handler_archivo.setLevel(logging.ERROR)
# Vamos a mantener el mismo formato
handler_archivo.setFormatter(formato_logs)
# Añadimos el handler al logger
logger.addHandler(handler_archivo)
# Creamos logger de tipo inforátivo
logger.info("Registro Informativo")
