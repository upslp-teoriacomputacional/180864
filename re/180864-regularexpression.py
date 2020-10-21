import re                                 # for performing regex expressions

tokens = []                               # for string tokens
source_code = 'int result = 1;'00.split() # turning source code into list of words

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