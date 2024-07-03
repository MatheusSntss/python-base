#!/usr/bin/env python3 
"""Spam básico python

Usando formatação & Interpolação
"""
__version__ = "0.1.0"
__author__ = "Matheus B."

email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Há apenas %(quantidade)d %(produto)s
com o valor R$ %(valor).2f!
Clique agora em %(link)s 
 """

clientes = ["José", "João" , "Matheus"]

# {} ----> dicionário
for cliente in clientes: 
    print(email_tmpl % {"nome":cliente,"produto":"Action Figure","quantidade":3,
    "link":"https//brinquedotoys.com.br","valor":60.5})
