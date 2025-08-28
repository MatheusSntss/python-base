#!/usr/bin/env python3
import logging

logger = logging.getLogger("meu_logger")
logger.setLevel(logging.DEBUG)

# Criando um handler para o console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatando a saída
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Associando o handler ao logger
logger.addHandler(console_handler)



logger.debug("Mensangem para o dev")
logger.info("Mensagem para o usuario")
logger.warning("Aviso que não causa erro")
logger.error("Erro que afeta uma unica execução")
logger.critical("Erro geral ex: Banco de dados sumiu")


try:
    1/0
except ZeroDivisionError as e:
    print(f"{str(e)}")
