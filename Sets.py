# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:48:53 2026

@author: Afra
"""

# Sets — Unique Collections
# Unique Elements
# Sets automatically remove duplicates. Unordered, so no indexing. Elements must be hashable (immutable).
# 🔗Set Operations
# Union (|), Intersection (&), Difference (-), Symmetric Difference (^) — just like mathematical sets.
# ⚡Fast Membership
# O(1) lookup time for 'in' checks. Much faster than lists for large collections.
#========================================================# Creating sets
s = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3])
print(from_list) # {1, 2, 3}

# Adding & removing
s.add(6)
s.discard(1) # no error if missing
s.remove(2) # KeyError if missing
print(s) # {3, 4, 5, 6}

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # Union: {1,2,3,4,5,6}
print(a & b) # Intersection: {3,4}
print(a - b) # Difference: {1,2}
print(a ^ b) # Symmetric diff: {1,2,5,6}

# Subset & superset
print({1,2}.issubset(a)) # True
print(a.issuperset({1,2})) # True
#=============================================================

# Remove duplicates from a list
nums = [1, 3, 5, 3, 1, 7, 5, 9]
unique = list(set(nums))
print(unique) # [1, 3, 5, 7, 9]

# Find common elements
skills_a = {"Python", "SQL", "ML"}
skills_b = {"Python", "Java", "ML", "Cloud"}
common = skills_a & skills_b
print(common) # {'Python', 'ML'}

# Frozen set (immutable set)
fs = frozenset([1, 2, 3])
# fs.add(4) → AttributeError!

# Set comprehension
evens = {x for x in range(20) if x%2==0}
print(evens)

# Practical: count unique words
text = "the cat sat on the mat"
words = set(text.split())
print(f"{len(words)} unique words: {words}")