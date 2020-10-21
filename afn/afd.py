#!/usr/bin/python
# -*- coding: utf-8 -*-

#
from sys import exit
import re
indice = 0
#Definimos la funcion caracter 
def caracter(character):
    global simbolo
    simbolo=""
    global Fin
    Fin=""
    letra_A = "(a)"
    letra_B = "(b)"
    epsilon = "[\w.%+-]"
    #digito="[0-9]"
    #operador="(\+|\-|\*|\/)"
    
    #comparar si es a o b
    if(re.match(letra_A,character)):
       simbolo="Letra_A"
       return 0
    else:
        if(re.match(letra_B,character)):
           simbolo="Letra_B"
           return 1
        else:
            if (re.match(epsilon,character)):
                simbolo="epsilon"
                return 2
            else:
                if (character==""):
                    simbolo = "\u03B5"
                    return 3
            
        print("Error el ",character,"no es valido")
        exit()
       
#definimos al la funcion  encabezado
def encabezado():
    print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
    body()

#definimos la funcion contenido donde guarda cada valor despues de encontrarlo en un ciclo
def contenido(estadosig,character,simbolo,estado):
    print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
    body()

#solo muestra la linea que se repetira cada vez que la mandemos a llamar
def body():
    print("+--------------+---------+-----------+---------------+")

#MAIN
    
#Tabla de transiciones
#---------------------#
#A->   a   b   ε   ""  
#0->   1   1   1   1
#1->   2   2   2   2
#2->   2   3   E   E
#3->   3   A   E   A
#--------------------#
    
    
#Este es la tabla de transiciones del automata AFD creado
tabla=[[ 1, 1, 1, 1],[2, 2, 2, 2],[2, 3, 'E', 'E'],[3, 'A', 'E', 'A']]
estado = 0

print ("""+-------------------------------------+
|    Ingrese una cadena a evaluar:    |
+-------------------------------------+""")
cadena = input()
#character=cadena
body()
encabezado()

if (cadena==""):
    character="\u03B5"
    cadena="\u03B5"
#else:
#    character=cadena[indice]
#ciclo para recorrer la cadena
while indice < len(cadena):
    
    character=cadena[indice]
   
#while cadena !="" :
    estadosig=estado
    
    #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
    charcaracter= caracter(character)
    
    #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
    estado=tabla[estado][charcaracter]
    
    #incremento del indice
    
    if (estado==3) and (character=="b"):
        indice += 1
    
    if (estado==2) and (character=="a"):
        indice += 1
    
    if (estado==3) and (character=="a"):
        indice += 1
        
    
    #Si el valor obtenido es una E imprimimos cadena no valida
    if (estado=="E"):
        print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
        body()
        print("""|              Cadena No Valida E                     |
+----------------------------------------------------+""")
        exit()
    #si el estado es A es una cadena de aceptacion
    #type(str(estado))
    if(estado=="A"):
        print("|     ",estado,"      |         |    FND    |               |")
        body()
        print("""|            Estado valido - Cadena Valida           |
+----------------------------------------------------+""")
    contenido(estadosig,character,simbolo,estado)

#al concluir si el estado no es 3 que es el de aceptacion imprimimos cadena no valida    
if(estado!=3):
        print("""|              Cadena No Valida Q                     |
+----------------------------------------------------+""")
#al estar en el estado 2  es el no valido imprimimos estado no valido    
if(estado==2):
        print("""|              Estado NO Valido                      |
+----------------------------------------------------+""")
#si el estado es 3 es una cadena de aceptacion
if(estado==3):
    print("|     ",estado,"      |         |    FND    |               |")
    body()
    print("""|            Estado valido - Cadena Valida           |
+----------------------------------------------------+""")
