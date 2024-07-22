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

import os
#Ler variavel de ambiente - 
import sys 
#ler variavel do sistema
arguments = {"lang":None,"count":1}
for arg in sys.argv[1:]:
    # TODO: Tratar valueError
     key,value = arg.split("=")
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


#Cli --
print(msg[current_language] * int(arguments["count"]))
