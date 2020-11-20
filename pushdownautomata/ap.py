"""
Useful unicode symbols in engineering
unicode	character	description
\u0394	Δ	GREEK CAPITAL LETTER DELTA
\u03A9	Ω	GREEK CAPITAL LETTER OMEGA
\u03C0	π	GREEK SMALL LETTER PI
\u03F4	ϴ	GREEK CAPITAL THETA SYMBOL
\u03BB	λ	GREEK SMALL LETTER LAMDA
\u03B8	θ	GREEK SMALL LETTER THETA
\u03B1	°	DEGREE SYMBOL
i\u0302	î	i HAT
j\u0302	ĵ	j HAT
k\u0302	k̂	k HAT
u\u0302	û	u HAT
Greek lower case letters
unicode	character	description
\u03B1	α	GREEK SMALL LETTER ALPHA
\u03B2	β	GREEK SMALL LETTER BETA
\u03B3	γ	GREEK SMALL LETTER GAMMA
\u03B4	δ	GREEK SMALL LETTER DELTA
\u03B5	ε	GREEK SMALL LETTER EPSILON
\u03B6	ζ	GREEK SMALL LETTER ZETA
\u03B7	η	GREEK SMALL LETTER ETA
\u03B8	θ	GREEK SMALL LETTER THETA
\u03B9	ι	GREEK SMALL LETTER IOTA
\u03BA	κ	GREEK SMALL LETTER KAPPA
\u03BB	λ	GREEK SMALL LETTER LAMDA
\u03BC	μ	GREEK SMALL LETTER MU
\u03BD	ν	GREEK SMALL LETTER NU
\u03BE	ξ	GREEK SMALL LETTER XI
\u03BF	ο	GREEK SMALL LETTER OMICRON
\u03C0	π	GREEK SMALL LETTER PI
\u03C1	ρ	GREEK SMALL LETTER RHO
\u03C2	ς	GREEK SMALL LETTER FINAL SIGMA
\u03C3	σ	GREEK SMALL LETTER SIGMA
\u03C4	τ	GREEK SMALL LETTER TAU
\u03C5	υ	GREEK SMALL LETTER UPSILON
\u03C6	φ	GREEK SMALL LETTER PHI
\u03C7	χ	GREEK SMALL LETTER CHI
\u03C8	ψ	GREEK SMALL LETTER PSI
\u03C9	ω	GREEK SMALL LETTER OMEGA
Greek upper case letters
unicode	character	description
\u0391	Α	GREEK CAPITAL LETTER ALPHA
\u0392	Β	GREEK CAPITAL LETTER BETA
\u0393	Γ	GREEK CAPITAL LETTER GAMMA
\u0394	Δ	GREEK CAPITAL LETTER DELTA
\u0395	Ε	GREEK CAPITAL LETTER EPSILON
\u0396	Ζ	GREEK CAPITAL LETTER ZETA
\u0397	Η	GREEK CAPITAL LETTER ETA
\u0398	Θ	GREEK CAPITAL LETTER THETA
\u0399	Ι	GREEK CAPITAL LETTER IOTA
\u039A	Κ	GREEK CAPITAL LETTER KAPPA
\u039B	Λ	GREEK CAPITAL LETTER LAMDA
\u039C	Μ	GREEK CAPITAL LETTER MU
\u039D	Ν	GREEK CAPITAL LETTER NU
\u039E	Ξ	GREEK CAPITAL LETTER XI
\u039F	Ο	GREEK CAPITAL LETTER OMICRON
\u03A0	Π	GREEK CAPITAL LETTER PI
\u03A1	Ρ	GREEK CAPITAL LETTER RHO
\u03A3	Σ	GREEK CAPITAL LETTER SIGMA
\u03A4	Τ	GREEK CAPITAL LETTER TAU
\u03A5	Υ	GREEK CAPITAL LETTER UPSILON
\u03A6	Φ	GREEK CAPITAL LETTER PHI
\u03A7	Χ	GREEK CAPITAL LETTER CHI
\u03A8	Ψ	GREEK CAPITAL LETTER PSI
\u03A9	Ω	GREEK CAPITAL LETTER OMEGA
\u03F4	ϴ	GREEK CAPITAL THETA SYMBOL
"""
#!/usr/bin/python
#import os
"""
First you need create a automata file where you define your productions, start states and stuff like that.

Q P F # total states
a # input word symbols
Z Y # stack symbols
Q # starting state
Z # starting stack
F # accepting states
F # E - accepts with empty stack or F - accepts with accepting state
Q a Z Q YZ # list of productions (current state, read from word, take from stack, next state, add to stack)
Q a Y Q YY
Q e Z P Z
Q e Y P Y 
P a Z P e 
P a Y P e
P e Z F e
notes:

We agree that "e" means epsilon and will not show up as state symbol.
You shouldn't use stack symbols that are longer than one character anything else is fine.
"""
start_input = "" # input word to be found or not found
found = 0 # stores found state
accepted_config = [] # here we will post end configuration that was accepted


# production rules ("read input", "pop stack", "push stack", "next state")
productions = {}

# all states or non-terminals (not really necessary)
states = []

# list of alphabet symbols or terminals (not really necessary)
symbols = []

# list of stack alphabet symbols (not really necessary)
stack_symbols = []

# start state
start_symbol = ""

# start stack symbol
stack_start = ""

# list of acceptable states
acceptable_states = []

# E - accept on empty stack or F - acceptable state (default is false)
accept_with = ""



# rcursively generate all prossiblity tree and terminate on success
def generate(state, input, stack, config):
	global productions
	global found

	total = 0

	# check for other tree node sucess
	if found:
		return 0

	# check if our node can terminate with success
	if is_found(state, input, stack):
		found = 1 # mark that word is accepted so other tree nodes know and terminate

		# add successful configuration
		accepted_config.extend(config)

		return 1

	# check if there are further moves (or we have to terminate)
	moves = get_moves(state, input, stack, config)
	if len(moves) == 0:
		return 0

	# for each move do a tree
	for i in moves:
		total = total + generate(i[0], i[1], i[2], config + [(i[0], i[1], i[2])])  

	return total


# checks if symbol is terminal or non-terminal
def get_moves(state, input, stack, config):
	global productions

	moves = []

	for i in productions:

		if i != state:
			continue

		for j in productions[i]:
			# print j
			current = j
			new = []

			new.append(current[3])

			# read symbol from input if we have one
			if len(current[0]) > 0:
				if len(input) > 0 and input[0] == current[0]:
					new.append(input[1:])
				else:
					continue
			else:			
				new.append(input)

			# read stack symbol
			if len(current[1]) > 0:
				if len(stack) > 0 and stack[0] == current[1]:
					new.append(current[2] + stack[1:])
				else:
					continue
			else:
				new.append(current[2] + append)

			moves.append(new)

	return moves


# checks if word already was generated somewhere in past
def is_found(state, input, stack):
	global accept_with
	global acceptable_states

	# check if all symbols are read
	if len(input) > 0: 
		return 0

	# check if we accept with empty stack or end state
	if accept_with == "E":
		if len(stack) < 1:  # accept if stack is empty
			return 1

		return 0

	else:
		for i in acceptable_states:
			if i == state: # accept if we are in terminal state
				return 1

		return 0


# print list of corrent configuration
def print_config(config):
	for i in config:
		print (i) 


def parse_file(filename):
	global productions
	global start_symbol
	global start_stack
	global acceptable_states
	global accept_with

	try:
		lines = [line.rstrip() for line in open(filename)]

	except:
		return 0

	# add start state
	start_symbol = lines[3]

	# add start stack symbol
	start_stack = lines[4]

	# list of acceptable states
	acceptable_states.extend(lines[5].split())

	# E - accept on empty stack or F - acceptable state (default is false)
	accept_with = lines[6] 

	# add rules
	for i in range(7, len(lines)):
		production = lines[i].split()

		configuration = [(production[1], production[2], production[4], production[3])]

		if not production[0] in productions.keys(): 
			productions[production[0]] = []

		configuration = [tuple(s if s != "e" else "" for s in tup) for tup in configuration]

		productions[production[0]].extend(configuration)

	print (productions)
	print (start_symbol)
	print (start_stack)
	print (acceptable_states)
	print (accept_with)

	return 1


# checks if symbol is terminal or non-terminal
def done():
	if found:
		print ("Hurray! Input word \"" + start_input + "\" is part of grammar.") 
	else:
		print ("Sorry! Input word \"" + start_input + "\" is not part of grammar.") 



# UI
# here it should read automata in from file
filename = input("Please enter your automata file:\n")
while not parse_file(filename):
	print ("File not found!")
	filename = input("Please enter your automata file again:\n")
print ("Automata built.")

start_input = input("Please enter your word:\n")
print ("Checking word \"" + start_input + "\" ...")

while start_input != "end":
	# magic starts here
	if not generate(start_symbol, start_input, start_stack, [(start_symbol, start_input, start_stack)]):
		done()
	else:
		print_config(accepted_config) # show list of configurations to acceptance
		done()

	start_input = input("Enter your next word (or end):\n")
	print ("Checking word \"" + start_input + "\" ...")