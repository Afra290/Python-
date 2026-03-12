# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:34:30 2026

@author: Afra
"""

# Tuples — Immutable Sequences
# Immutable
# Once created, tuples cannot be changed. No adding, removing, or modifying elements. This makes them hashable and usable as dict keys.
# ⚡Faster than Lists
# Tuples are more memory efficient and faster to iterate. Use them for fixed collections of data.
# 📦Packing & Unpacking
# Easily pack values into a tuple and unpack them into variables. Great for returning multiple values from functions.
# #=======================================================
# Creating tuples
point = (3, 4)
colors = ("red", "green", "blue")
single = (42,) # trailing comma needed!
from_list = tuple([1, 2, 3])

# Accessing (same as lists)
print(colors[0]) # red
print(colors[-1]) # blue
print(colors[0:2]) # ('red', 'green')

# Unpacking
x, y = point
print(f"x={x}, y={y}") # x=3, y=4

# Swap values
a, b = 10, 20
a, b = b, a
print(a, b) # 20 10

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last) # 1 [2,3,4] 5

# Cannot modify!
# point[0] = 5 → TypeError!
#==========================================================
# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2)) # 3
print(nums.index(3)) # 2

# Concatenation & repetition
a = (1, 2)
b = (3, 4)
print(a + b) # (1, 2, 3, 4)
print(a * 3) # (1, 2, 1, 2, 1, 2)

# Length & membership
print(len(nums)) # 6
print(2 in nums) # True

# Tuples as dict keys (hashable)
locations = {
(0, 0): "Origin",
(1, 0): "East",
(0, 1): "North"
}
print(locations[(0, 0)]) # Origin

# Named tuples (better readability)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y) # 3 4