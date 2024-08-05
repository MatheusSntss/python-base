#!usr/bin/env python3 
"""
Problema: Ir a padaria comprar pão:
Permissa: Padaria da Esquina abre fds: até as 12h, semana até as 19h,
feriado (exceto Natal) não abre.
"""
__version__ = "0.1.0"
import sys
print("A padaria está aberta?\n")
feriado = input("É feriado? E NÃO é natal\n").lower()
fds = input("É sábado OU domingo e antes do meio dia?\n ").lower()
semana = input("É dia de semana e antes das 19h?\n").lower()

if(feriado == "nao"):
    print("Padaria está aberta!")
elif(fds == "sim"):
    print("a padaria está aberta!")
elif(semana == "sim"):
    print("Padaria está aberta!")
    
else:
    print("está fechada!")
aberta = True
if(aberta):
    chuva = input("Está chovendo?")
    if(chuva == "sim"):
        print("Pegar guarda chuva")
        calor = input("está calor ?")
        if(calor == "sim"):
            print("pegar guarda-chuva e garrafa de água")
        frio = input("esta frio?")
        if(frio == "sim"):
            print("pegar guarda-chuva e casaco")
    print("ir até a padaria")
    baguete = input("Tem pão baguete?")
    integral = input("Tem pão integral?")

    if(baguete and integral == "sim"):
        print("6 de cada")
    elif(baguete or integral == "sim"):
        print("12 paes")
    else:  
        print("6 de qualquer um ")
else: 
    print("ficar em casa e comer bolacha")
   

