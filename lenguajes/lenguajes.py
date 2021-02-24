# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:23:44 2021

@author: el_racional
"""
#Operaciones con cadenas

SingleQuotes ='Python in Single Quotes'  
DoubleQuotes ="Python in Double Quotes"  
print(SingleQuotes)  
print(DoubleQuotes) 
message = "Hello, Python!"  

print(message[7])  

#Text            =   P Y T H O N   
# Positive Index =   0 1 2 3 4 5   
# Negative Index = -(6 5 4 3 2 1)  

Text = 'PYTHON'  
print(Text[3])  
Text = 'PYTHON'  
print(Text[-4])  
message = 'Hello, Python'  
print(message[7:10])  

message ="    Welcome Python.  "  
print (message.strip())  

message ="Welcome Python!"  
print (message.lower())  

message ="Python tutorial with dotnettechpoint.com"  
print (message.upper())  

message ="Welcome Python!"  
print (len(message))  

message ="Python with dotnettechpoint.com"  
print (message.replace("Python","Learn Python"))  

message ="Python, tutorials, with, dotnettechpoint.com"  
print (message.split(","))  

message ="python tutorials with dotnettechpoint.com"  
print (message.title())  

message ="python tutorials with dotnettechpoint.com"  
print (message.capitalize())  

message ="python tutorials with dotnettechpoint.com"  
print (message.count('t'))  

message ="Python tutorials with dotnettechpoint.com"  
print (message.find('with'))  

message ="Python Tutorials"  
print(" ".join(message))  

first_string ="Python"  
last_string = "Tutorial"  
print (first_string +" " +last_string)

first_string ="Python "  
middle_string ="3"  
last_string = "Tutorial"  
print (first_string +" "+middle_string+" " +last_string) 

first_string ="Python "  
middle_string =3  
last_string = "Tutorial"  
print (first_string +" "+str(middle_string)+" " +last_string)  

























