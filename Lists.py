# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:15:56 2026

@author: Afra
"""

# Lists — Ordered Collections
# Mutable & Ordered
# Lists are ordered, changeable collections that allow duplicates. Defined with square brackets [ ]. Can hold mixed types.
# 🔍Accessing Elements
# Access by index (0-based), slice with [start:stop:step], iterate with for loop, or use list comprehensions.
# 🛠️List Methods
# append(), insert(), remove(), pop(), sort(), reverse(), extend(), index(), count(), copy(), clear().


#===============================================
# Creating lists
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1,2], [3,4], [5,6]]
empty = []

# Accessing
print(nums[0]) # 1
print(nums[-1]) # 5
print(nums[1:4]) # [2, 3, 4]
print(nested[1][0]) # 3

# Updating
nums[0] = 99
print(nums) # [99, 2, 3, 4, 5]

# Adding elements
nums.append(6) # add to end
nums.insert(0, 0) # add at index
nums.extend([7, 8]) # add multiple
print(nums)

# Removing elements
nums.remove(99) # remove by value
popped = nums.pop() # remove last
del nums[0] # remove by index
print(nums)


#======================================================
# Sorting
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort() # in-place
print(nums) # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True) # descending
print(nums) # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() returns new list
original = [3, 1, 4]
new = sorted(original)
print(original) # [3, 1, 4] (unchanged)

# Other methods
nums = [1, 2, 3, 2, 1]
print(nums.count(2)) # 2
print(nums.index(3)) # 2
nums.reverse()
print(nums) # [1, 2, 3, 2, 1]

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]


# Filter with comprehension
evens = [x for x in range(10) if x%2==0]
print(evens) # [0, 2, 4, 6, 8]

# Unpacking
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest) # 1 2 [3, 4, 5]