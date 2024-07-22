#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala que frenquenta
cada uma das atividades.
"""
__version__ = "0.0.1"
__author__ = "Matheus"

# Dados
sala1 = ["Matheus","Andre","Guilherme","Adrieli","Karen","Isaque"]
sala2 = ["João","Larissa","Marcos","Pedro","Paulo"]

aula_ingles = ["Matheus","Marcos","João","Larissa"]
aula_espanhol = ["Marcos","Karen","Andre"]
aula_muaythai = ["Matheus","Andre","Guilherme"]


#Tupla com laibel
atividades ={
    "Inglês": aula_ingles,
    "Espanhol": aula_espanhol, 
    "Muay thai": aula_muaythai,
}

# Listar alunos em cada atividade por sala.

for chave, valor in atividades.items():
    print(f"Alunos da atividade de {chave}\n")


    atividade_sala1 = set(sala1) & set(valor)
    atividade_sala2 = set(sala2) & set(valor)

    
    
    print(f"Alunos sala 1", atividade_sala1)
    print(f"Alunos sala 2", atividade_sala2)
    print()
    print("-" * 30)
    print()
    
