# loggin no requiere instalacion, nos muestra los logs o registros de los códigos que desarrollamos.
import logging
# cada log que se imprime, tiene tres partes, laprimera, el nivel de seguridad, segunga el logger y la ultima mensaje:
# WARNING:root:Log de advertencia
# ERROR:root:Log de error
# CRITICAL:root:Log de error crítico

# Para definir el primer nivel de los logs que queremos usar
logging.basicConfig(level = logging.DEBUG, filename="ejemplo_logs.log", filemode="w")

logging.debug("Log de debugging")
logging.info("Log Informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")