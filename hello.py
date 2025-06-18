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

#Dunder
__version__ = "0.0.1"
__author__ = "Matheus Santos"
__version__ = "Unlicense"

current_language = os.getenv("LANG","en_US")[:5]
msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Ola, mundo!"
elif current_language =="it_IT":
    msg = "Ciao, Mondo!"
    
print(msg)
