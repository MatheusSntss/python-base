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

Os resultados serão salvos em logs `infixcal.log`
"""
import sys
import os
import logging
from datetime import datetime

logger = logging.getLogger("meu_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler() 
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


__version__ = "0.1.1"


operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

argumentos = sys.argv[1:]

if not argumentos:
    operacao = input("Operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    argumentos = [operacao, n1, n2]
elif len(argumentos) != 3:
    print("Quantidade de argumentos inválido")
    print("ex `num 5 5`")
    sys.exit(1)

operacao, *nums = argumentos



if operacao not in operacoes:
    print("A operação não existe")
    print(operacoes.keys())
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

resultado = operacoes[operacao](n1,n2)

print(f"O resultado é: {resultado}")

path = os.curdir
filepath = os.path.join(path,"infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER","anonymous")
try:
    with open(filepath,"a") as file_:
        file_.write(f"{timestamp} - {user} - {operacao},{n1},{n2} = {resultado}\n")
except PermissionError as e:
    logger.error("Você não tem permissão para criar o arquivo, %s",str(e))
