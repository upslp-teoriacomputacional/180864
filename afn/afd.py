#!/usr/bin/python
# -*- coding: utf-8 -*-

#https://www.tutorialspoint.com/python_data_structure/python_graphs.htm#:~:text=A%20graph%20can%20be%20easily,the%20values%20in%20the%20dictionary.
import sys
import ast 

def main():
    transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
    input = raw_input("enter the string: ")
    input = list(input) #copy the input in list because python strings are immutable and thus can't be changed directly
    for index in range(len(input)): #parse the string of a,b in 0,1 for simplicity
        if input[index]=='a':
            input[index]='0' 
        else:
            input[index]='1'

    final = "3" #set of final states = {3}
    start = 0
    i=0  #counter to remember the number of symbols read

    trans(transition, input, final, start, i)
    print ("rejected")



def trans(transition, input, final, state, i):
    for j in range (len(input)):
        for each in transition[state][int(input[j])]: #check for each possibility
            if each < 4:                              #move further only if you are at non-hypothetical state
                state = each
                if j == len(input)-1 and (str(state) in final): #last symbol is read and current state lies in the set of final states
                    print ("accepted")
                    sys.exit()
                trans(transition, input[i+1:], final, state, i) #input string for next transition is input[i+1:]
        i = i+1 #increment the counter


main()