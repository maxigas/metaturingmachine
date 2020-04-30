#!/usr/bin/python3

def reverter(string):
    '''Original reverter'''
    # Accumulate the output in this variable:
    Reversion = "" 
    for number in string:
        if number in "1":
            # Same as below, but using a compound assignment operator
            # Reversion += "0"
            Reversion = Reversion + "0"
        if number in "0":
            Reversion = Reversion + "1"
    return Reversion

def reverter2(string):
    '''Reverter implemented with list comprehension'''
    return ''.join("0" if x is "1" else "1" if x is "0" else "" for x in string)

def reverter3(i,o=""):
    '''Recursive reverter'''
    if len(i) is 0:
        return o
    else:
        if i[0] is "0":
            o += "1"
        elif i[0] is "1":
            o += "0"
        return reverter3(i[1:], o)

def reverter4(i,o=""):
    '''Recursive reverter with ternary assignment'''
    if len(i) is 0:
        return o
    else:
        o += "0" if i[0] is "1" else "1" if i[0] is "0" else ""
        return reverter4(i[1:], o)
  
print(reverter(input("Enter a String of 0 and 1 and it will be reverted! Everything else will be skipped: ")))
