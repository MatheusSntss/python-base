#!/usr/bin/env python3
import logging
from logging import handlers
logger = logging.getLogger("meu_logger")
logger.setLevel(logging.DEBUG)

# Criando um handler para o console

# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEB)
file_handler = handlers.RotatingFileHandler("meulog.log",maxBytes=10**6)
file_handler.setLevel(logging.DEBUG)
# Formatando a saída
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Associando o handler ao logger
logger.addHandler(file_handler)


"""
logger.debug("Mensangem para o dev")
logger.info("Mensagem para o usuario")
logger.warning("Aviso que não causa erro")
logger.error("Erro que afeta uma unica execução")
logger.critical("Erro geral ex: Banco de dados sumiu")
"""

try:
    1/0
except ZeroDivisionError as e:
    logger.debug("Erro division by zero")
