#!/usr/bin/env python3

"""
Imprime mensagem de um e-mail
"""
__version__ = "0.1.1"
import os
import sys


argumentos = sys.argv[1:]
if not argumentos:
    print("Informe o  nome do arquivo de emails")
    sys.exit(1)

filename = argumentos[0]
file_tmpl = argumentos[1]
path = os.curdir
filepath = os.path.join(path,filename) #email.txt
templatepath = os.path.join(path,file_tmpl) #email_tmpl.txt
for line in open(filepath):
    nome,email=line.split(",")
    
    print(f"Enviando e-mail para:{email}")
    print()
    print(
        open(templatepath).read()
            %{
            "nome":nome,
            "produto":"Caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade":3,
            "preco": 2.25
        }
    )
    print("-" * 50)
