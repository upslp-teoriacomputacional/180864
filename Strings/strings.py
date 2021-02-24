# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:24:25 2021
This program validate chars to alphabet {a-z} and digits {0-9}
No validate Upper Case and special characters blank spaces
@author: jc-gi
"""
import re #Regular expression 
def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))

#execute this command in terminal

special_match("")#the result its true

special_match("az09.") #the result its true

special_match("az09.\n")#the result is false

# The above test case is to catch out any attempt to use re.match()
# with a `$` instead of `\Z` -- see point (6) below.
special_match("az09.#")
special_match("az09.X")

