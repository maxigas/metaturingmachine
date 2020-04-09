#!/usr/bin/python3
# Import some metaprogramming libraries and random.
import ast, astpretty, dis, inspect, random

import random

def turingmachine():
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



# 0. Print source code of function.
print(inspect.getsource(turingmachine))

# 1. Print AST (Abstract Syntax Tree) of function
astpretty.pprint(ast.parse(inspect.getsource(turingmachine)))
print(); print("-"*80)

# Disassemble function.
dis.dis(turingmachine)
print(); print("-"*80)

# Run function.
turingmachine()
print(); print("-"*80)

