#!/usr/bin/env python3

import logging

#TODO: usar funcao
#TODO: usar lib
# nossa instancia 
log = logging.Logger("logs.py", logging.DEBUG)

# level 
ch = logging.StreamHandler() # Manda para o console / terminal
ch.setLevel(logging.DEBUG)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s, %(name)s, %(levelname)s, l:%(lineno)d f:%(filename)s: %(message)s '
)
ch.setFormatter(fmt)

#destino
log.addHandler(ch)
log.debug("Mensagem pro dev,qe,sysadmin")
log.info("Mensagem geral para o usuario")
log.warning("Aviso que não causa erro. Ex: o python3 vai mudar a partir da semana que vem") # msg so aparece do warning para baixo
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral, Ex: BAnco de dados sumiu")
