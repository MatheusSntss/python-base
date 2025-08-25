#!/usr/bin/env python3

"""
Imprime mensagem de um e-mail
"""
__version__ = "0.1.0"

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preço promocional R$%(preco).2f
"""
clientes = ["Maria","Marta","Joao"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome":cliente,
            "produto":"Caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade":3,
            "preco": 2.25
        }
    )
