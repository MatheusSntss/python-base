#!/usr/bin/env python3
"""Hello World Multi Linguages

Depeding on the language configured in the environment, the program displays 
the corresponding language

Usage:
Have a properly configured variable LANG exemple:
    export LANG=pt_BR
    
Execution:
    python3 hello.py
        or
    ./hello.py
"""

import os
import sys
import logging

logger = logging.getLogger("meu_logger")
logger.setLevel(logging.DEBUG)

# Criando um handler para o console
console_handler = logging.StreamHandler() #Manda pro console
console_handler.setLevel(logging.INFO)

# Formatando a saída
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Associando o handler ao logger
logger.addHandler(console_handler)

#Dunder
__version__ = "0.1.3"
__author__ = "Matheus Santos"
__version__ = "Unlicense"


arguments = {
    "lang" : None,
    "count" : 1,
}

for arg in sys.argv[1:]:
    try:
        key,value = arg.split("=")
    except ValueError as e:
        #TODO: usar Logging
        logger.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
            )
        sys.exit(1)                   
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"] 
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Choose language:")   

current_language = current_language[:5]

msg = {
    "en_US":"Hello World!",
    "pt_BR":"Olá Mundo!",
    "fr_FR":"Bonjour, Monde!"
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"{e}")
    print(f"Language is invalid, choose from: {list(msg.key())}")
print(msg[current_language] * int(arguments["count"]))

# Ordem Complexidade O(n)
# if current_language == "pt_BR":
#     msg = "Ola, mundo!"
# elif current_language =="it_IT":
#     msg = "Ciao, Mondo!"
