# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:25:29 2026

@author: Afra
"""

# Iterate over a list
fruits=["apple","banana","mango"]
for fruit in fruits:
    print(fruit)

# range() function
for i in range(5): # 0 to 4
 print(i, end=" ")
 print()
 # 0 1 2 3 4

for i in range(2, 10, 3): # start, stop, step
   print(i, end=" ")
   print() # 2 5 8

# Enumerate (index + value)
for i,fruit in enumerate(fruits):
    print(f"{i}:{fruit}")

# Iterate over string
for char in "Python":
    print(char,end="-")
# P-y-t-h-o-n-

# List comprehension
Squares=[x**2 for x in range(6)]
print(Squares)# [0, 1, 4, 9, 16, 25]

even=[x for x in range (20) if x%2==0]
print(even)