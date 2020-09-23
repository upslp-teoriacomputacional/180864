## Python Program to Illustrate Different Set Operations

  <li>Los tres operadores lógicos básicos son O, Y y NO, representados en Python por or, and y not, respectivamente.

Podemos incluir también el O EXCLUSIVO, que es verdadero cuando uno y solo uno de los operandos lo es, pero estrictamente debes saber que se deriva a partir de los tres básicos. Su representación es ^, el sombrero o caret.

Como ejercicio práctico, vamos a realizar un programa que construya las tablas de verdad correspondientes.
"""</li>

 
</ol>
La variable x recorrerá la lista booleanos, tomando en la primera iteración el valor False y en la siguiente True. 
Pero, por cada iteración, aparece una nueva variable y que también recorrerá booleanos de izquierda a derecha. 
Así garantizamos que se alcanzan las cuatro combinaciones posibles de x e y.

En la impresión con print, hemos empleado el argumento sep = ‘t’ para que separe cada elemento mediante un tabulador, 
en lugar de usar un espacio en blanco, valor por omisión. Aprecia el uso de la expresión x or y para que muestre el resultado del or.

El resto de las tablas se calcula del mismo modo, simplemente teniendo en cuenta que hay que emplear, naturalmente, 
la expresión lógica adecuada.

Debes saber que los operadores lógicos de Python son del tipo cortocircuitados, término que quizás te resulte familiar 
si conoces otros lenguajes de programación. Esto significa que, si a partir del primer operando ya se puede deducir el 
resultado final, Python ni se molestará en evaluar el segundo, con el consiguiente ahorro de tiempo.

En un or, si el primer operando es verdadero, sabemos que el resultado lo será ya, por lo que no es necesario que Python 
se moleste en comprobar la veracidad del segundo.

Del mismo modo, en un and, si el primer operando es falso, el resultado inmediatamente lo será y tampoco será necesario 
saber lo que ocurre con el segundo.

Para finalizar, una pequeña advertencia: es un error común confundir los operadores lógicos (or y and) con los operadores 
de unión e intersección de conjuntos (| y &).
<p></p>

## Source Code

```python

# Comenzamos creando una lista con los dos posibles valores booleanos, False y True, 
# que utilizaremos para iterar sobre ellos:
booleanos = [False, True]
#Observa que no hemos rodeado los elementos entre comillas, pues no son strings.
#A continuación imprimimos los títulos para la operación or:

# Tabla de verdad de or

# Los \t en la primera línea no son más que tabuladores. La extraña operación de la segunda, 
# multiplicando un string por un número, no hace más que repetir 22 veces el carácter ‘-‘.
print('x\ty\tx or y')
print('-'*22)

# El quid de la cuestión recae en la doble iteración usando el bucle for: 
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep = '\t')

```
## Help - ?


<small> <a href="" target="\_blank"></a> </small>


Visit <a href="https://github.com/upslp-teoriacomputacional/180864/" target="\_blank"> (Programming set in Python).

<small>@jc-gi<a href="https://github.com/jc-gi" target="\_blank"></a> for the language support! </small>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
