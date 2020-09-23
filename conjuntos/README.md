## Python Program to Illustrate Different Set Operations

  <li>1. In this example, we have defined two set variables and we have performed different set operations: union, intersection, difference and symmetric difference.,  </li>
  <li>2. To understand this example, you should have the knowledge of the following Python programming topics:  </li>
  <li>3.Python Sets  </li>
  <li>4. Python Input, Output and Import  </li>
  <li>Python offers a datatype called set whose elements must be unique. It can be used to perform different set operations like union, intersection, difference and symmetric difference. </li>
  <li>Is the Quadratic Allocation Problem NP-complete or is it in P? Either give a reduction to show it is NP-complete or give a polytime algorithm to solve it. </li>

 
</ol>
Aside: This problem arose during some consulting I was doing, where the integers represented the sizes of different software jobs, and the quadratic term is there because the cost of implementing software goes up faster than linearly with the size of the job. 
<p></p>

## Source Code

```python

# - 180864-conjuntos.py *- coding: utf-8 -*-
"""
Set Section
# Program to perform different set operations like in mathematics
#Find to similar command to other language
#Rust, F# and Perl
"""
    
# define three sets
global A
global B
global C

A = set([1,2,3,4,5]) 
B = set([3,4,5,6,7]) 
C = {}

print("The set is:", A)
print("The set B is : ", B)
print("The set C is :", C)

#%%
#Remove an item from the set
def quitar():
    A.discard(2)
    print("The set after to delete: ", A)

#%%
#Remove all items from the set
def clearSet():
    A.clear() 
    print("The set clear: ", A)

#%%
#Copy a set
def copiar():
    B=A.copy() 
    print("Set A = ", A, " compare set B = ", B)

#%%Add an item
def agregar():
    B.add(987) 
    print("The new set B = ", B) 
#%%%
"""
Set Operations
"""
#%%
#Union
def union():
    print("The union = ", A|B) 
    print("The union = ", A.union(B))
#%%
#Intersection
def intereseccion():
    print("The intersection = ", A&B)
    print(A.intersection(B))

#%%
#Diference
def diferencia():
    print("The diference = ", A-B)
    print("The intersection = ", A.difference(B))

#%%
#Symmetric difference
def simetrica():
    print("The symmetric_difference = ", A^B)
    print("The symmetric_difference = ",A.symmetric_difference(B))
    print("The symmetric_difference = ",B.symmetric_difference(A))
    print("The symmetric_difference = ",A.symmetric_difference(C))
    print("The symmetric_difference = ",B.symmetric_difference(C))

#%%
#Subset
def subconjunto():
    print("The subset = ",A.issubset(B))
    print("The subset = ",B.issubset(A))

#%%
#Superset
def superconjunto():
    print("The superset = ",B.issuperset(A))
    print("The supersrt = ",A.issuperset(B)) 



"""
Python has lists. The empty list is []. The following is a list of one
item ["a"] and so is [3]. Here is a list with 3 items ["ball",3.14,-2]. Let's
define a list, I'll call it lis and we'll do things with it to illustrate
accessing items in a list. Execute the following cell with Ctrl-Enter.
"""


```
## Help - ?

In this program, we take two different sets and perform different set operations on them. This can equivalently done by using set methods.
<small> <a href="" target="\_blank">@</a> for this feature!</small>


Visit <a href="https://github.com/upslp-teoriacomputacional/180864/" target="\_blank"> (Programming set in Python).

<small>@jc-gi<a href="https://github.com/jc-gi" target="\_blank"></a> for the language support! </small>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
