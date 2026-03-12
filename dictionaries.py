# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:45:24 2026

@author: Afra
"""

# Dictionaries — Key-Value Mapping
# 🔑Key-Value Pairs
# Unordered (insertion-ordered since 3.7) collection of key:value pairs. Keys must be unique and hashable. Values can be any type.
# ⚡O(1) Lookup
# Dictionary lookups are extremely fast (constant time). Use them when you need to map identifiers to data.
# 🔧Dict Methods
# get(), keys(), values(), items(), update(), pop(), setdefault(), and dictionary comprehensions.
# # Creating dicts
person = {
"name": "Alice",
"age": 25,
"skills": ["Python", "SQL"]
}

# Accessing values
print(person["name"]) # Alice
print(person.get("age")) # 25
print(person.get("job", "N/A")) # N/A (default)

# Modifying
person["age"] = 26 # update
person["job"] = "Engineer" # add new
del person["skills"] # delete

# Iterating
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key} → {value}")

# Keys & values
print(list(person.keys()))
print(list(person.values()))
#====================================================
# Dictionary methods
d = {"a": 1, "b": 2, "c": 3}

# pop — remove & return
val = d.pop("b")
print(val, d) # 2 {'a': 1, 'c': 3}

# update — merge dicts
d.update({"c": 30, "d": 4})
print(d) # {'a': 1, 'c': 30, 'd': 4}

# setdefault
d.setdefault("e", 5) # adds if missing
d.setdefault("a", 99) # keeps existing
print(d)

# Dict comprehension
squares = {x: x**2 for x in range(6)}
print(squares) # {0:0, 1:1, 2:4, ...}

# Nested dict
students = {
"s1": {"name": "Bob", "grade": "A"},
"s2": {"name": "Eve", "grade": "B"},
}
print(students["s1"]["name"]) # Bob

# Check existence
print("a" in d) # True
print(5 in d.values()) # True