#Alfabeto aceptado
A = ['a','b']
#Bandera por si la entrada no pertenece
#al alfabeto de entrada
bandera = True
#Tabla de transición
TablaT = [[0,'a',0],[0,'b',1],[1,'a',1]]
#transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
#transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
#Tabla de estados de la comparación
TablaC = []
#Estados finales
EF = [1]
#Estado inicial
E = 0
#Estado Actual
EA = E
#Cadena de entrada
CE = "aba"
#Recorremos la Cadena de entrada
for c in CE:
    print(c)
    #Verificamos que sea del alfabeto aceptado
    if c in A:
        print("Esta en el alfabeto")
        #Buscamos en la tablaT
        for f in TablaT:
            #Recorrido de las producciones
            #Buscamos el estado actual y el caracter de entrada
            if c in f and EA in f:
                #Agregamos a la tabla final
                TablaC.append([EA,c,f[2]])
                #print(f[2])
                #Actualizamos el estado actual
                EA = f[2]
                print("Estado Actual: "+str(EA))
    else:
        print("Cadena no pertenece al alfabeto")
        bandera = False
#Comparamos el estado final
#Para saber si es terminal y se acepta
#o no la cadena de entrada.
if EA in EF and bandera == True:
    print("---------------------------------\n")
    print("Se acepta la cadena de entrada!!!\n")
    print("-----Tabla de transiciones-------\n")
    for t in TablaC:
        print(t)
else:
    print("No se acepta la cadena de entrada!!!\n")
    print("-----Tabla de transiciones-------\n")
    for t in TablaC:
        print(t)