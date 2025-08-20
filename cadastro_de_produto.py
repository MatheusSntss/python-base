#!/usr/bin/env python3

"""
Cadastro de produto
"""
__version__ = "0.1.0"
from pprint import pprint

produto = {
    "nome": "caneta",
    "cores": ["azul","branco"],
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "preco": 3.23,
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,    
}

cliente = {
    "nome": "Matheus",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}
total = compra['produto']['preco'] * compra['quantidade']
print(
    f"O cliente {compra['cliente']['nome']} comprou uma {compra['produto']['nome']}"
    f" e pagou o total de R${total}"
)
