#!/usr/bin/env python3

"""Cadastro de produto
"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome":"Homem de giz",
    "tipo": "Livro",
    "categoria": ["Drama","Suspense"],
    "valor": 31.5,
    "estoque":True,
    "codigo": 341,
    }


cliente ={
    "nome":"Matheus",
    "Sobrenome":"Santos",
    "id":192,
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

total_compra = compra["quantidade"] * compra["produto"]["valor"] #traversing

print(
    f"O cliente {compra['cliente']['nome']} " 
    f"comprou {compra['produto']['nome']} "
    f"e pagou o total de R$ {total_compra}"
    )
