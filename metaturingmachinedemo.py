#!/usr/bin/python3
# Sample code for the Computing Cultures tutorial at UVA, 2020 Amsterdam

# Depends on metaprogramming libraries and random
import ast, astpretty, dis, inspect, random

def turingmachine():
    '''A minimal Turing Machine

    This implementation uses an 8 bit long tape.  The tape is initialised by
    random Boolean values.  It can be thought of as a single line punch tape.
    The configuration of the machine is contained in the head() function.  It
    flips bits, e.g. changes True to False, and False to True.  The head()
    function is implemented recursively, so there is no need for another named
    variable and a for loop.  The claim behind this implementation choice is
    that it is closer to the original idea of Turing then a more
    idiomatic/Pythonic way of doing it.
    '''
    tape=random.choices(population=(True,False), k=8)
    for x in tape:
        print(x, end='|', flush=True)
    print()
    # for x in tape: print(not x, end='|', flush=True)
    def head(tape):
        """Recursive version of the above for loop"""
        if tape:
            print(not tape[0], end="|", flush=False)
            head(tape[1:])

    head(tape)

# The program makes itself visible as a kind of visualisation of the Turing Machine

# 0. Print source code of function
print(inspect.getsource(turingmachine))

# 1. Print AST (Abstract Syntax Tree) of function
astpretty.pprint(ast.parse(inspect.getsource(turingmachine)))
print(); print("-"*80)

# 2. Disassemble function
dis.dis(turingmachine)
print(); print("-"*80)

# 3. Run function
turingmachine()
print(); print("-"*80)

# One may remember that every Turing Machine is cabable to simulate all other
# Turing Machines... each of these code representations (0-3) is fed to a
# different Turing Machine, simulated by the previous Turing Machine...

