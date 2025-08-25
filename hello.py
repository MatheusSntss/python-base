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
#Dunder
__version__ = "0.1.3"
__author__ = "Matheus Santos"
__version__ = "Unlicense"


arguments = {
    "lang" : None,
    "count" : 1,
}

for arg in sys.argv[1:]:
    # TODO Tratar ValueError
    key,value = arg.split("=")
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

print(msg[current_language] * int(arguments["count"]))

# Ordem Complexidade O(n)
# if current_language == "pt_BR":
#     msg = "Ola, mundo!"
# elif current_language =="it_IT":
#     msg = "Ciao, Mondo!"
