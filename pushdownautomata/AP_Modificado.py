
# Universidad Politecnica de San Luis Potosi
# Alumno: Saul Hernandez Lara
# Matricula: 151062
# Teoria Computacional
# Ingenieria en Tecnologias de la Informacion

# Automata de pila que valida cadenas (0i1i+k2k3n+1) tal que i,k,n > 0
# Cadenas validas:  011233, 00111122333
#por cada 0 se inserta un X a la pila
#por cada 1 se inserta Y en la pila
#por cada 2 se borra una X
#por cada 3 se borra una Y

pushdown = []

def scanner(string):
    global pushdown
    state = 1
    rtn = False

    pushdown.append('Z') # Simbolo inicial

    for char in string:
        state = move(state, char)

    if (state == 4 or state == 5) and pushdown[-1] == 'Z':    # Eliminacion de simbolo inicial
        pushdown.pop()
        state = 6

    if state == 6 and pushdown == []:
        rtn = True

    return rtn

def move(state, symbol):
    global pushdown
    rtn = 0

    value = pushdown[-1]

    if state == 1 and symbol == '0' and value == 'Z':
        pushdown.append('A')
        rtn = 1

    if state == 1 and symbol == '0' and value == 'A':
        pushdown.append('A')
        rtn = 1

    if state == 1 and symbol == '1' and value == 'A':
        if pushdown:
            pushdown.pop()
            rtn = 2

    if state == 2 and symbol == '1' and value == 'Z':
        pushdown.append('B')
        rtn = 2

    if state == 2 and symbol == '1' and value == 'B':
        pushdown.append('B')
        rtn = 2

    if state == 2 and symbol == '1' and value == 'A':
        if pushdown:
            pushdown.pop()
            rtn = 2

    if state == 2 and symbol == '2' and value == 'B':
        if pushdown:
            pushdown.pop()
            rtn = 3

    if state == 3 and symbol == '2' and value == 'B':
        if pushdown:
            pushdown.pop()
            rtn = 3

    if state == 3 and symbol == '3' and value == 'Z':
        pushdown.append('D')
        rtn = 4

    if state == 4 and symbol == '3' and value == 'D':
        if pushdown:
            pushdown.pop()
            rtn = 5

    if state == 5 and symbol == '3':
        print("no me muevo")
        rtn = 4

    return rtn

phrase = input("Escriba una cadena y oprima enter: ")
string = list(phrase)

if scanner(string):
    print("Cadena valida")

else:
    print("Cadena no valida")