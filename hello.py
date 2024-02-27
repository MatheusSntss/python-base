#!/usr/bin/env python3
"""
Hello  Word Multi Linguas

Como usar:
Tenha o LANG devidamente configurado
Ex: LANG=pt_br

Modo de uso:
	python3 hello.py
	./hello.py
"""
__version__ = "0.0.1"
__author__ = "Matheus Santos"
__license__ = "Unlicense"

import os
 
current_linguage = os.getenv("LANG", "en_US")[:5]

msg = "Hello Word!" 
if current_linguage == "pt_BR":
	msg = "Ola mundo!"

print (msg)
