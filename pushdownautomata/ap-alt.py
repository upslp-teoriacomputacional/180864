# -*- coding: utf-8 -*-
#!/usr/bin/python
""" 
	Practica 6 
	Automata de Pila
	
	
"""
import os 
from sys import exit
def validar(val):
	flag = 0
	for x in val:
		if x != "0" and x != "1":
			flag = 1
	if flag == 1:
		print ("Esta palabra no es valida tiene que ser de la forma: ")
		print ("{0°n 1°n | n >= 0}")
		exit()
	else :
		poscicion = val.find("1")
		recorre_unos = val[poscicion: ]
		recorre_ceros = val[:poscicion]
		for y in recorre_unos:
			if y == "0":
				print ("Esta palabra no es valida tiene que ser de la forma: ")
				print ("{0°n 1°n | n >= 0}")
				exit()
		if len(recorre_unos) != len(recorre_ceros):
			print ("Esta palabra no es valida tiene que ser de la forma: ")
			print ("{0°n 1°n | n >= 0}")
			exit()
		

def automata_de_pila(val):
	pila = ["#"]
	alfabeto_pila = "a"
	print ("Palabra del alfabeto: ",val	)
	print ("Estado inicial de la pila: ",pila)	
	print ()
	print ()
	for i in val:
		if i == "0":
			pila.append(alfabeto_pila)
			print ("Se lee un ",i," en la pila y se INSERTA una a")
			print ("pila: ",pila)
			print
		if i == "1":
			pila.pop()
			print ("Se lee un ",i," en la pila y se EXTRAE una a")
			print ("pila: ",pila)
			print
	print ("Queda vacía la pila lo cual indica que es correcta la palabra del alfabeto")
							
		
os.system('clear')
os.system('cls')		
print ("Automata de pila de la forma:")
print ("Alfabego de la pila = {#,a}")
print ("{0°n 1°n | n >= 0}")

valores = input("Escriba los valores:")
validar(valores)
automata_de_pila(valores)