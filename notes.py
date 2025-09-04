#!/usr/bin/env python3 
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
tex: 
Anotação geral sobre carreira de tecnologia

$notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"
import os
import sys
# Pega todos os argumentos passados pelo usuário, ignorando o nome do script (sys.argv[0]).
arguments = sys.argv[1:]
operactions = ["new","read"]

#Verifica se há argumento, caso não haja aparece a mensagem de erro
if not arguments: 
    print("Erro, falta o argumento")
    sys.exit(1)
#Verifica se o primeiro argumento passado pelo usuário é valido, caso não seja da erro
if arguments[0] not in operactions:
    print("Operação invalida")
    print(operactions)
    sys.exit(1)

#Referenciando o diretorio atual
path = os.curdir 
filepath = os.path.join(path,"nota.txt")


try:
    title = arguments[1]
except IndexError as e:
        print(f"{e}")
        print("Faltou o segundo argumento")
        sys.exit(1)
if arguments[0] == "new":
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:").strip()
    ]
    with open(filepath,"a") as file_:
        file_.write("\t".join(text) + "\n")
else: 
    for line in open(filepath):
        title,tag,text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()
