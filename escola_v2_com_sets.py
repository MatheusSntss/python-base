#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.

"""
__version__ = "0.1.1"

#Dados
sala1 = ["Erik","Maia","Gustavo","Manoel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria"]

atividade_ingles = ["Erik", "Maia","Joana","Carlos","Antonio"]
atividade_musica = ["Erik", "Carlos","Maia"]

atividades = [
    ("Inglês",atividade_ingles), 
    ("Música",atividade_musica),
    ]


#Lista alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 30)
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)
    print(f"Sala 1:{atividade_sala1}")
    print(f"Sala 2:{atividade_sala2}")
    print("-" * 30)
    print()
