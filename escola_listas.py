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
atividades = [
    ("Inglês", aula_ingles),
    ("Espanhol", aula_espanhol), 
    ("Muay thai", aula_muaythai)
]

# Listar alunos em cada atividade por sala.

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade de {nome_atividade}\n")
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"Alunos sala 1", atividade_sala1)
    print(f"Alunos sala 2", atividade_sala2)
    print()
    print("-" * 30)
    print()
    
# Listar alunos em cada atividade por sala

# aula_ingles_sala1 = []
# aula_ingles_sala2 = []
# 
# for aluno in aula_ingles:
    # if aluno in sala1:
        # aula_ingles_sala1.append(aluno)
    # elif aluno in sala2:
        # aula_ingles_sala2.append(aluno)
# 
# print("Alunos sala 1", aula_ingles_sala1)
# print("Alunos sala 2",aula_ingles_sala2)

