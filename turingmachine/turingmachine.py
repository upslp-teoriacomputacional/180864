"""
Tape
Cabezal (apuntador,simboloa sobreescribir,izquierda-derecha-izquierda)
Registro de estados
Tabla de transiciones
La maquina de turing tiene las caracteristicas de un Automata finito

Q = Es un conjunto de estados
    Σ = Alfabeto conjunto de caracteres (codigo utf-8 ="\u03A3")	
    Γ = Simbolos de la cinta
    s = Estado inicial sϵQ
    δ= Reglas nde transicion (Codigo utf-8 = "\u03B4")
    QxΣ->Q Reglas de transicion
    bϵΓ = es un simbolo denominado blanco, que se puede repetir 
          infinitamente en toda la cinta 
    F⊆Q Estado finales o de aceptacion
    
    Q = {s,q1}
    Σ = {a}	
    Γ = {a,b}
    s = Estado inicial q0ϵQ
    δ= Reglas de transicion 
    Reglas de transicion
    Q x Σ -> Q
    ((q0,a)->q1*)
    (estado, valor) -> nuevo estado, nuevo valor, dirección)
    (s,a)->q1,b,right
    (q1,b)->--Valido--
    "si estamos en el estado s leyendo la posición q1, donde hay 
    escrito el símbolo 'a', entonces este símbolo debe ser reemplazado 
    por el símbolo 'b', y pasar a leer la celda siguiente, a la derecha".
    F⊆Q = {q1}
    
    Estructura gafica es un grafo dirigido que se conecta en los vertices 
    con:
        (lee el cabezal/
        símbolo que escribirá el cabezal, 
        movimiento del cabezal.)
        (s,a)->q1,b,right
        ('a',b,right)
        
"""

def turing_M (state = None, #estados de la maquina de turing
              blank = None, #simbolo blanco de el alfabeto dela cinta
              rules = [],   #reglas de transicion
              tape = [],    #cinta
              final = None,  #estado valido y/o final
              pos = 0):#posicion siguiente de la maquina de turing

    st = state
    if not tape: tape = [blank]
    if pos <0 : pos += len(tape)
    if pos >= len(tape) or pos < 0 : raise Error ("Se inicializa mal la posicion")
    
    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)
    """
Estado	Símbolo leído	Símbolo escrito	       Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
"""
    while True:
        print (st, '\t', end=" ")
        for i, v in enumerate(tape):
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")
        print()
        
        if st == final: break
        if (st, tape[pos]) not in rules: break
        
        (v1,dr,s1) = rules [(st, tape[pos])]
        tape[pos]=v1 #rescribe el simbolo de la cinta
    
    #movimiento del cabezal
        if dr == 'left':
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape): tape.append(blank)
        st = s1

print("Maquina de turing Test")

#se puede cambiar las reglasde transicion para otra maquina de turing
turing_M (state = 'p', #estado inicial de la maquina de turing
              blank = 'b', #simbolo blanco de el alfabeto dela cinta
              tape = list("1011"),#inserta los elementos en la cinta
              final = 'q',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "p 1 x right p".split(),
                          "p 0 0 right p".split(),
                          "p b b right q".split(),
                          ]   
                         )
             )    


print("Maquina de turing Incremento")
turing_M (state = 'q0', #estado inicial de la maquina de turing
              blank = 'b', #simbolo blanco de el alfabeto dela cinta
              tape = list("11111111x111111111111111111111111111111111111="),#inserta los elementos en la cinta
              final = 'q9',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "q0 1 1 right q0".split(),
                          "q0 x x right q0".split(),
                          "q0 = = left q1".split(),
                          "q1 1 Y left q2".split(),
                          "q1 x x right q8".split(),
                          "q2 1 1 left q2".split(),
                          "q2 x x left q2".split(),
                          "q2 Z Z left q2".split(),
                          "q2 b b right q3".split(),
                          "q3 Z Z right q3".split(),
                          "q3 1 Z right q4".split(),
                          "q3 x x left q6".split(),
                          "q4 1 1 right q4".split(),
                          "q4 x x right q4".split(),
                          "q4 Y Y right q4".split(),
                          "q4 = = right q4".split(),
                          "q4 b 1 left q5".split(),
                          "q5 = = left q5".split(),
                          "q5 Y Y left q5".split(),
                          "q5 1 1 left q5".split(),
                          "q5 x x left q5".split(),
                          "q5 Z Z left q2".split(),
                          "q6 Z 1 left q6".split(),
                          "q6 b b right q7".split(),
                          "q7 x x right q7".split(),
                          "q7 1 1 right q7".split(),
                          "q7 Y Y left q1".split(),
                          "q8 = = right q5".split(),
                          "q8 1 1 right q5".split(),
                          "q8 Y 1 right q5".split(),
                          "q8 b b right q9".split(),
                          ]   
                         )
             )  


       