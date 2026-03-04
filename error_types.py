# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:12:15 2026

@author: Afra
"""

# TYPES OF ERROR

#SyntaxError

print("Hello)

try:
    print("Hello)  # Press Ctrl+D (Unix) or Ctrl+Z+Enter (Windows) to raise EOFError
except SyntaxError as e: # syntaxerror cannot catch  with (try & except) because it occurs before execution.
    print("This is new error",e)
   


    def greet():
    print("Hi")


# IndentationError

try:
    def greet():
    print("Hi")
except IndentationError as e:
    print("This is new error :1",e)



# NameError
try:
   print(age)   # Press Ctrl+D (Unix) or Ctrl+Z+Enter (Windows) to raise EOFError
   
except NameError as e:
    print("This is new error :1",e)

#Zero division error

19/0

try:
    print(19/0)
except ZeroDivisionError as e:
    print("This is new error :2-",e, "it is infinity \n and numbers cannot be divided by zero!")