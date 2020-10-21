## Programación expresiones regulares 
### Importancia de los lenguajes regulares.
  <li>La existencia y formalización de los lenguajes regulares (LR) y su vinculación con otros artefactos lingüísticos-matemáticos ya bien formalizados, estudiados e incluso llevados a la práctica ha sido de vital importancia en el ulterior desarrollo de los mecanismos de procesamiento de lenguajes de computadora, fundamentalmente en los analizadores lexicográficos gracias a la posibilidad de derivar el reconocimiento de los LR mediante autómatas finitos que son fáciles de implementar computacionalmente con mecanismos simples y rápidos, óptimos en la obtención de parsers veloces y robustos que a su vez le ofrecen a los desarrolladores información detallada de los errores léxicos, sintácticos e incluso advierten sobre errores semánticos.
Lo mismo sucede por ejemplo con las expresiones regulares implementadas ya en muchos Lenguaje de programación de propósito general modernos que permiten a los desarrolladores de lenguajes mecanismos muy eficientes para la obtención intuitiva de partes de compiladores que reconocen los tókenes o partículas lexicales del código fuente como fase del proceso completo de interpretación o compilado, según sea el caso.
A manera de ilustración en el caso del ejemplo anterior vemos la siguiente función Python que a partir de cualquiera de los elementos formalizadores del LR correspondiente permite decidir si un texto w es una variable PROLOG:  </li>

## Source Code

```python

def variablePROLOG(w):
        '''(str)-->bool. True si "w" es un nombre de variable correcto'''
        if (w[0].isalpha and w[0]==w[0].upper()) or w[0]=='_':
                #El primer caracter es una mayuscula o un subrayado
                w = w[1:] #Se quita el primer caracter
                while w and (w[0].isalnum() or w[0]=='_'):
                        #Mientras queden caracteres en "w" y el primer caracter actual sea un alfanumerico o un subrayado, todo esta bien
                        w = w[1:] #Quitar el primer caracter
                if w=='':
                        #Si ya no quedan elementos a revisar, es una variable PROLOG
                        return True
        return False


```
  
<p> </p>
Varias funciones de esa naturaleza componen los analizadores lexicográficos para discriminar la función de cada token del lenguaje en cuestión: constante númerica, literal de cadena de texto, identificador, separador, etc.; según sea el caso.
Y también puede verse que existe una estrecha relación en cómo implementar las funciones reconocedoras de LR y la expresión o la gramática regulares o el autómata finito correspondiente, al punto que desde hace más de 3 décadas existen aplicaciones generadoras de analizadores lexicográficos como el Flex o el Bisonte.
Pero el alcance de los LR no se queda en el mundo de la compilación de lenguajes de ordenador como se ve en el siguiente ejemplo.
<p> </p>

## Programación generadora gramática regular

<p> </p>


<ol>
Analizador léxico simple
Ejemplo#
En este ejemplo, te mostraré cómo hacer un lexer básico que creará los tokens para una declaración de variable entera en Python.
¿Qué hace el analizador léxico?
El propósito de un lexer (analizador léxico) es escanear el código fuente y dividir cada palabra en un elemento de la lista. Una vez hecho esto, toma estas palabras y crea un par de tipo y valor que se parece a esto ['INTEGER', '178'] para formar un token.
Estos tokens se crean para identificar la sintaxis de su idioma, por lo que todo el objetivo del lexer es crear la sintaxis de su idioma, ya que todo depende de cómo desee identificar e interpretar los diferentes elementos.
</ol>

### Source Code

```python

import re                                 # for performing regex expressions
int result = 100;

tokens = []                               # for string tokens
source_code = 'int result = 100;'.split() # turning source code into list of words

# Loop through each source code word
for word in source_code:
    
    # This will check if a token has datatype decleration
    if word in ['str', 'int', 'bool']: 
        tokens.append(['DATATYPE', word])
    
    # This will look for an identifier which would be just a word
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])
    
    # This will look for an operator
    elif word in '*-/+%=':
        tokens.append(['OPERATOR', word])
    
    # This will look for integer items and cast them as a number
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';': 
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else: 
            tokens.append(["INTEGER", word])

print(tokens) # Outputs the token array



```

Cuando se ejecuta este fragmento de código, la salida debe ser la siguiente:

```python
[['DATATYPE', 'int'], ['IDENTIFIER', 'result'], ['OPERATOR', '='], ['INTEGER', '100'], ['END_STATEMENT', ';']]

```
Vamos a descomponerlo
1.	Comenzamos con la importación de la biblioteca de expresiones regulares porque será necesario cuando se compruebe si ciertas palabras coinciden con un determinado patrón de expresiones regulares.
2.	Creamos una lista vacía llamada tokens. Esto se utilizará para almacenar todos los tokens que creamos.
3.	Dividimos nuestro código fuente, que es una cadena en una lista de palabras donde cada palabra en la cadena separada por un espacio es un elemento de la lista. Luego los almacenamos en una variable llamada source_code .
4.	Comenzamos a recorrer nuestra lista de source_code palabra por palabra.
5.	Ahora realizamos nuestro primer control:
6.	if word in ['str', 'int', 'bool']: 
7.	   tokens.append(['DATATYPE', word])
Lo que buscamos aquí es un tipo de datos que nos dirá qué tipo de variable será nuestra variable.
8.	Después de eso, realizamos más verificaciones como la anterior, identificando cada palabra en nuestro código fuente y creando un token para ella. Estos tokens se pasarán al analizador para crear un árbol de sintaxis abstracta (AST).


## Help - ?



Visit <a href="https://github.com/upslp-teoriacomputacional/180864/" target="\_blank"> (Programming in Python).

<small>@jc-gi<a href="https://github.com/jc-gi" target="\_blank"></a> for the language support! </small>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
