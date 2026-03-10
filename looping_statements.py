# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:30:16 2026

@author: Afra
"""

# Basic while loop
count = 0
while count <=5:
    print(count, end=" ")
    count += 1
# 0 1 2 3 4

# break — exit loop early
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
    print() # 0 1 2 3 4

# continue — skip iteration
for i in range(8):
    if i % 2 == 0:
        continue
    print(i, end=" ")
    print() # 1 3 5 7

# pass — placeholder (do nothing)
for i in range(5):
    if i == 3:
       pass # TODO: handle later
    else:
        print(i, end=" ")
        print() # 0 1 2 4

# for-else (runs if no break)
for n in [2, 4, 6]:
     if n % 2 != 0:
        print("Found odd!")
        break
     else:
         print("All even!")