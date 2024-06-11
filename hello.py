#!/usr/bin/env python3
"""Hello word Multi Linguas

Dependendo da lingua configuradano ambiente o programa exibe a mensagem
correspondente.

Como usar: 
Tenha a variavel LANG devidamente configurada ex:

    LANGUAGE=en_US
Execucao:
    python3 hello.py
ou
    ./hello.py
"""

__version__="0.0.1"
__author__="Matheus Santos"
__license__= "unlicense"
# Dunder

import os
#Ler variavel de ambiente - 

# Este programa imprime hello word


current_language = os.getenv("LANG")[:5]
# snake case
msg = "Hello,Word"

if current_language == "pt_BR":
    msg = "Ola, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, mondo!"

print(msg)
