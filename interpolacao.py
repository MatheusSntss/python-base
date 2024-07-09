#!/usr/bin/env python3 
"""Spam básico python

Usando formatação & Interpolação
"""
__version__ = "0.1.0"
__author__ = "Matheus B."


#old style
"""email_tmpl =
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Há apenas %(quantidade)d %(produto)s
com o valor R$ %(valor).2f!
Clique agora em %(link)s 

clientes = ["José", "João" , "Matheus"]

# {} ----> dicionário
for cliente in clientes: 
    print(email_tmpl % {"nome":cliente,"produto":"Action Figure","quantidade":3,
    "link":"https//brinquedotoys.com.br","valor":60.5})
"""

#new style 
#metodo format
email = "Olá {nome}, Tem interesse em comprar {produto}? Há apenas {num} {produto} com o valor de R$ {valor} Clique agora em {link}"
print(email.format(nome="Matheus",produto="Caneta",num=5,valor=10.5,link="https//brinquedotoys.com.br"))
