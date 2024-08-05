#!/usr/bin/env python3
"""Hello word Multi Linguas

Dependendo da lingua configuradano ambiente o programa exibe a mensagem
correspondente.

Como usar: 
Tenha a variavel LANG devidamente configurada ex:

    LANGUAGE=en_US
Ou informe através do CLI argument ´--lang´

Execucao:
    python3 hello.py
ou
    ./hello.py
"""

__version__="0.1.1"
__author__="Matheus Santos"
__license__= "unlicense"
# Dunder
import logging 

log = logging.Logger("hello.py", logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    '%(asctime)s, %(name)s, %(levelname)s, l:%(lineno)d f:%(filename)s: %(message)s '
)
ch.setFormatter(fmt)
log.addHandler(ch)

import os
#Ler variavel de ambiente - 
import sys 
#ler variavel do sistema
arguments = {"lang":None,"count":1}
for arg in sys.argv[1:]:
    # TODO: Tratar valueError
    try:
        key,value = arg.split("=")

    except ValueError as e:
        #TODO:Logging
        log.error("you need '=', you passed %s, try --key=value: %s ",arg,str(e))
 
        sys.exit(1)
        
    key = key.lstrip("-").strip() 
    if key not in arguments:
        print (f"Invalid Option ´{key}´")
        sys.exit()
    arguments[key] = value
     
current_language = arguments["lang"]

if current_language is None:    
    current_language = os.getenv("LANG")
    # TODO : usar repetição
    if current_language is None: 
        current_language = input("Choose language:")

current_language = current_language[:5]


msg = { 
    "en_US": "Hello, World",
    "pt_BR": "Olá Mundo",
    "it_IT": "Ciao, Mundo",
    "es_SP": "Hola, Mundo"
 }

# message = msg.get(current_language,msg["en_US"])
try:
    message = msg[current_language]
except KeyError:
    print(f"Language is invalid, try {msg}")
    sys.exit(1)

#Cli --
print(message * int(arguments["count"]))
