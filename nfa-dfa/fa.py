# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:44:24 2020

@author: el_racional
"""


"""
Automata finito se compone de:
    Definicion formal:
        
    Q = Es un conjunto de estados
    Σ = Alfabeto conjunto de caracteres (codigo utf-8 ="\u03A3")	
    q0 = Estado inicial q0ϵQ
    δ= Reglas nde transicion (Codigo utf-8 = "\u03B4")
    QxΣ->Q Reglas de transicion
    F⊆Q Estado finales o de aceptacion
   
    Representacion de un automata finito es:
        Representación como diagramas de estados
        Por medio de un grafo
        O = un nodo
        ->=transicion 
        (vertice que une a un "nodo a" con un "nodo b")
        x = elemento que se envia de "nodo a a nodo b"
            a       x       b
        -->O-------------->O
        
        Vertices 'Q' son los nodos 'a' & 'b'
        δ = --------> && elemento es (x ϵ Σ)
        --> = estado inicial definido por q0
        F = un grafo encerrado en un circulo "oO"
        qf = estado final o de aceptacion
        
                          (x ϵ Σ) 
        Estado  --->O-------------->oO
        inicial     q0              F=qf
    Representación como tabla de transiciones
    
    Tabla de transiciones:
        La primera representa explícitamente los parámetros y el valor que toma cada ocurrencia de la función de transición
        
    salida(q∈Q)  símbolo(σ∈Σ) llegada(δ(q,σ)∈Q)
    ->q0            σ = 'x'         F=qf
    
    Matriz de estados:
       marca con una flecha el estado inicial, y con un asterisco los estados finales. 
        
       Estados/
        (x ϵ Σ)     x
        ->q0        qf
          qf *     NULL
            
Note que el estado inicial q0 
de un autómata finito siempre es único, en tanto que 
los estados finales pueden ser más de uno, es decir, 
el conjunto F puede contener más de 
un elemento. También puede darse el caso de que un 
estado final corresponda al mismo estado inicial.

    Cadena de caracteres pertenece a ese alfabeto
    Σ = {x}
    
    
 Σ* = conjunto de todas las cadenas de caracteres o palabras que se pueden conformar con dicho alfabeto.
 x* = {"",x,xx,xxx,xxxx,......xn}   
 δ* = QxΣ*->Q Reglas de transicion
 
 x ∈ Σ*, 
 todo símbolo a ∈ Σ, 
 un estado q ∈ Q:

cadena vacia = una cadena vacía o string vacío es la 
única cadena de caracteres de tamaño cero. 
Se denota usualmente con las letras griegas λ o ϵ.
Propiedades: 
La cadena vacía es el elemento neutro para la concatenación de elementos de un alfabeto Σ.
Al revertir una cadena vacía, obtendremos la misma cadena vacía.
es prefijo, sufijo y subcadena de toda cadena.

Representaqcion en python:
    "" O  '' O str()
    
    Recursividad:
       
        x= todas las cadenas generadas del Σ*
        a = definicion del caracter del Σ
        Σ = {x}       
        Σ*={"", x, xx, xxx, xxxx, .......xn}
        x = {x,xx,xxx,xxxx,}
        a = {x}
        δ*(q,ϵ) = q cuando la cadena es vacia 
        δ*(q,xa) = δ(δ*(q,x),a)
        
Autómata finito determinista
Que existan dos transiciones del tipo δ(q,a)=q1 y δ(q,a)=q2, siendo q1 ≠ q2;
Que existan transiciones del tipo δ(q, ε), salvo que q sea un estado final, sin transiciones hacia otros estados.

Autómata finito NO determinista
Que existan transiciones del tipo δ(q,a)=q1 y δ(q,a)=q2, siendo q1 ≠ q2;
Que existan transiciones del tipo δ(q, ε), siendo q un estado no-final, o bien un estado final pero con transiciones hacia otros estados.

en un AFND se define como:
δ = QxΣ->P(Q) 
Para el caso de los AFND-ε, se suele expresar la función de transición de la forma:
δ = Qx{ΣUϵ}->P(Q) 
donde P(Q) es el conjunto potencia de Q.

    Q = {q0,q2,q3,qf}
    Σ = {ϵ,x}	
    q0 = {q0}
    QxΣ->P(Q)  Reglas de transicion
    P(Q)={
    δ= (qo,ϵ) = q2 
    δ= (qo,x) = qf 
    δ= (q2,x) = q3
    δ= (q3,ϵ) = qf }
    F={qf}
    
    ***Nota***
Esto significa que los autómatas finitos deterministas 
son un caso particular de los no deterministas, 
puesto que Q pertenece al conjunto P(Q).

AFD⊆AFND

Un lenguaje regular sobre un alfabeto dado se define recursivamente como:

El lenguaje vacío es un lenguaje regular
El lenguaje cadena vacía {ε} es un lenguaje regular
Para todo símbolo a ∈ Σ {a} es un lenguaje regular
Si A y B son lenguajes regulares entonces A ∪ B (unión), A•B (concatenación) 
y A* (clausura o estrella de Kleene) son lenguajes regulares
Si A es un lenguaje regular entonces (A) es el mismo lenguaje regular
No existen más lenguajes regulares sobre Σ


Lenguaje vacio Regular
{ε} = regular
{x} =regular
A ∪ B (unión) A={a} && B={b} = {a} U {b}
A•B = {ab}
A* Cerradura de kleene cualquier número de cadenas del conjunto inicial, 
posiblemente con repeticiones, y concatenándolas entre sí de un Σ

x, xx, xxx, xxxx, xxxxxx, xxxxxxxx

A*={ε, a,aa, aaa, aaaa, aaaa....}

Expresion regular valido las operaciones de union concatenacion y
cerradura de kleene

(x U x.x U x.x.x.)*

Conversión de un AFND-ε a un AFD

Primer paso obtener Clausula ε AFND-ε

Clausula ε
->q0 = {q0 U q2}
q2 = {q2 U Ø} 
q3 = {q3 U q2,qf}
qf* = {qf U Ø}

Paso dos obtener la tabla de transiciones del AFND-ε

Tabla de transiciones
        Clausula ε              'x'
->q0        q2                  qf
q2          --                  q3 
q3        {q2,qf}               --
qf*          --                  --

Tercer paso obtner las transiciones para el AFD
                    x
{q0 U q2}        {q3 U q2,qf}
{q3 U q2,qf}     {q3 U q2,qf}

Retiquetar la tabla 
-> q0   = {q0 U q2}
   qf*  = {q3 U q2,qf}

Nueva tabla de transiciones del AFD
                x
    ->q0        qf
      qf        qf
      
Minimización de un AFD
Dos estados de un autómata finito determinista son estados 
equivalentes si al unirse en un solo estado, pueden reconocer
 el mismo lenguaje regular 
 
Lenguaje regular {x}*

Un AFD está minimizado, 
si todos sus estados son distinguibles (si son validos o noson validos)
y alcanzables (las transiciones van a estados iguales)

Son distinguibles

Validos = {q0,qf} --->   Distinguibles
No validos = {}

alcanzables

(q0,x)->Valido
(qf,x)->Valido

Reetiquetan en un solo estado
q0 = {q0,qf}

La nueva matriz seria
            x
->q0*       q0






 


Hacer un automata se usa JFLAP
"""

# Definicion del alfabeto 
Σ = ['x']

# Declaracion de la tabla de transicionesEstados/
#        δ(q0,x)=q1, δ(q1,'')=q1
#        Estados     x
#        ->q0        qf
#          qf *     NULL
#############################
#Tabla logica
#   -espacio de memoria- se conecte a otro espacio de memoria
#   -enviar un caracter entre espacios de memoria
#   Lista
#   '0' = Posicion actual del nodo
#   'x' = El dato de esa posicion
#   '1' = El siguiente nodo
#   Esta esla reperesentacion en python = [0,'x',1] 
#   Estados                     
#   q0 Posicionde me moria 0
#   qf Posicion de memoria 1 
#   'x' Caracter enviar de q0 a qf
##################################################
# Tabla es:
# 0     x       1
# 1     NA      NULL
#Transicion vacia tabla logica
# [0,'',1]
###################################################
#Tabla de transiciones
# TablaT=[[0,'x',1],[1, '', -1]]
TablaT=[[0,'x',0]]
#Utilizar una bandera para revisar que (x ϵ Σ)
bandera = True
#Tabla para almacenar los estado que se mueven
TablaC = []
#estado inicial q0 = posicion 0 de la tabla
EI = 0
#Estafo final qf = posicion 1 de la tabla 
EF=[0]
#Estado actual
EA = EI
#cadena de caracteres del alfabeto
print ("Inserta la cadena a evaluar")
cadena = input()

for caracter in cadena:
    print (caracter)
    #verificar que el caracter pertenezca a el Σ = ['x']
    if caracter in Σ:
        print ("El carcacter (x ϵ Σ) ")
        #Buscar en la tabla el caracter TablaT
        for f in TablaT:
            #Recorrer las transiciones de la tabla
            #Indicar el estado actual y el estado final
            if caracter in f and EA in f:
                #Agregar elementos a la tabla comparativa TablaC
                TablaC.append([EA,caracter,f[2]])  
                #actualizar el estado
                EA=f[2]
                print ("Estado actual es : " + str(EA))
    else:
        print("Cadena no pertenece al alfabeto")
        bandera = False

#Comparar si el estado actual es igual al estafo final

if EA in EF and (bandera == True):
    print("------------------------------")
    print("Es valida la cadena de entrada")
    print("____Tabla de transiciones_____")
    for t in TablaC:
        print (t)
else:
    print("---------------------------------")
    print("NO es valida la cadena de entrada")
    print("______Tabla de transiciones______")
    for t in TablaC:
        print (t)
        

        
    
        


























