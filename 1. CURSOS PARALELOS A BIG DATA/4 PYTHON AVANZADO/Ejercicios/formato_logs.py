# loggin no requiere instalacion, nos muestra los logs o registros de los códigos que desarrollamos.
import logging
# cada log que se imprime, tiene tres partes, laprimera, el nivel de seguridad, segunga el logger y la ultima mensaje:
# WARNING:root:Log de advertencia
# ERROR:root:Log de error
# CRITICAL:root:Log de error crítico

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
nombre = 'Paco'
logging.error(f"{nombre} creó el error")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")
# División por 0 que imprima el error
try:
    division = 2 / 0
except:
    #logging.error("División por cero")
    # Muestra mensaje y error ocurrido
    logging.exception("División por cero")
    