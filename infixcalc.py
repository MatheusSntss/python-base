#!usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

operações: 
sum -> + 
sub -> -
mul -> *
div -> /

uso: 
$ infixcalc.py sum 5 4
9

"""
import sys
import operator
__version__ = "0.1.0"


operacoes = ["sum","sub","mul","div"]

argumentos = sys.argv[1:]

if not argumentos:
    operacao = input("Operação:")
    n1 = int(input("n1:"))
    n2 = int(input("n2:"))
    argumentos = [operacao, n1, n2]
elif len(argumentos) != 3:
    print("Quantidade de argumentos inválido")
    print("ex `num 5 5`")
    sys.exit(1)

operacao, *nums = argumentos



if operacao not in operacoes:
    print("A operação não existe")
    print(operacoes)
    sys.exit(1)
    
numeros_validos = []
for num in nums:
    if not num.replace(".","").isdigit():
        print(f"Numéro invalido {num}")
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    numeros_validos.append(num)
n1,n2 = numeros_validos

if operacao == "sum":
    print(n1 + n2)
elif operacao == "sub":
    print(n1 - n2)
elif operacao == "mul":
    print(n1 * n2)
elif operacao == "div":
    print(n1 / n2)
