# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 20:54:14 2026

@author: Afra
"""

# Example 1: Function that returns None
def function_name(a, b, c):
    z = a * b + c
    return None
function_name(5,4,9)


# Example 2: Function that prints the result
def function_name(a, b, c):
    z = a * b + c
    print(z)
function_name(5,4,9)

# Example 3: Function with pass (does nothing)
def function_name(a, b, c):
    pass
function_name(5,4,9)

# Example 4: Function that returns the calculated value
def function_name(a, b, c):
    z = a * b + c
    return z
function_name(5,4,9)

# Example 5: Function that returns a dictionary
def function_name(a, b, c):
    z = a * b + c
    return {"result": z}
function_name(5,4,9)

# Example 6: Function that returns a tuple
def function_name(a, b, c):
    z = a * b + c
    return (a, b, c, z)
function_name(5,4,9)

# Example 7: Function with default parameters
def function_name(a=1, b=2, c=3):
    z = a * b + c
    return z
function_name(5,4,9)

# Example 8: Function with type hints
def function_name(a: int, b: int, c: int) -> int:
    z = a * b + c
    return z
function_name(5,4,9)

# Example 9: Function with docstring
def function_name(a, b, c):
    """
    Calculates z = a * b + c
   
    Parameters:
        a: first number
        b: second number
        c: third number
   
    Returns:
        The result of a*b + c
    """
    z = a * b + c
    return z
function_name(5,4,9)

# Example 10: Lambda equivalent
function_name = lambda a, b, c: a * b + c
function_name(5,4,9)



list_var = [2,4,6,8,10]

for i in list_var:
    print(i)















# Example 11: Function with error handling
def function_name(a, b, c):
    try:
        z = a * b + c
        return z
    except TypeError:
        return "Invalid input types"


# Example 12: Function using walrus operator (Python 3.8+)
def function_name(a, b, c):
    return (z := a * b + c)


# Example 13: Function with conditional return
def function_name(a, b, c):
    z = a * b + c
    if z > 100:
        return "Large"
    else:
        return "Small"


# Example 14: Function that modifies a global variable (not recommended)
result = 0

def function_name(a, b, c):
    global result
    result = a * b + c
    return result