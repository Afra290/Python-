# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:47:06 2026

@author: Afra
"""

var=[5]
for i in var:
    print(i**2)

#using lamda function
num_square=lambda x: x**2
print(num_square(5))

#sorting of list
nums=[3,1,4,1,5,9]
sorted(nums)

nums=[3,1,4,1,5,9]
print(sorted(nums,key=lambda x: -x))

#map,filter,reduce
doubled= list(map(lambda x: x*2,nums))
evens=list(filter(lambda x: x%2==0,nums))
print (doubled)
print(evens)

nums1=[2,3,7,4,6,9,10,2,3,8]
evens=list(filter(lambda x: x%2==0,nums1))
print(evens)