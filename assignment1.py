p# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 15:03:19 2026

@author: Afra
"""

SECTION A – VARIABLES & DATA TYPES

1.  Define variables of type: int float str bool complex
#     int- any number without decimal ,ex:4,-4
#     float-any number with decimal ,ex: 4.9,-4.9
#     str- collection of characters or single char ex:"Afra",'A'
#     bool-returns single value either True or False
#     complex-combination of both letters and numbers ex:(3-ij)


2.  Identify the data type of the following: a = 100 b = 45.67 c =
    “Python” d = True e = 3 + 4j
    a=100 #int
    b= 45.67 #float
    c="Python" #str
    d=True #bool
    e=3+4j #complex
3.  Write five valid identifiers.
    student_name="Afra"
    marks= 95
    age= 18
    my_variable="AK"
    _subject="DBMS"

4.  Correct the following invalid identifiers: 1name my-name class total
    marks @value
    # my-name=my_name
    # class=Class"""
    # total =TOTAL
    # marks=_marks
    # @value= value

SECTION B – INPUT & OUTPUT

5.  Write a program to take a student’s name and print: Welcome
    name=input("Enter Your name:")
    print(f"Welcome",name)

6.  Write a program to take two integers and print their sum.
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number"))
    print("Sum of the no is:",num1+num2)

7.  Write a program to take age as input and print: Your age is
    age=input("Enter your age:")
    print("Your age is:",age)

8.  Write a program to take a number and print its square.
    a=4
    sq=a*a
    print("the square of number is:",sq)

SECTION C – ARITHMETIC OPERATORS

9.  Write a program to perform: Addition Subtraction Multiplication
    Division Modulus of two numbers.
    a=4
    b=9
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)

10. Write a program to calculate area of a rectangle. Formula: Area =
    length * breadth
    length=4
    breadth=5
    area=length*breadth
    print("Area of a rectangle is:",area)

11. Write a program to convert Celsius to Fahrenheit. Formula: F = (C *
    9/5) + 32 
    C=int(input("enter the celsius:"))
    F=((C*9/5)+32)
    print("Fahrenheit",F)

12. Write a program to calculate Simple Interest. Formula: SI = (P *
    R * T) / 100
    amount=4500
    Rate=4
    Time=9
    Simp_interest=(amount*Rate*Time/100)
    print("The simple interest is:",Simp_interest)

SECTION D – RELATIONAL & LOGICAL OPERATORS

13. Write a program to check whether a number is positive or negative.
    a=int(input("enetr any number:"))
    if a>=0:
        print("Number is positive")
    else:
        print("Number is negative")

14. Write a program to check whether a number is even or odd.
    a=int(input("enetr any number:"))
    if a%2==0:
        print("Number is even")
    else:
        print("Number is odd")

15. Take two numbers and check: If both are greater than 10. If at least
    one is less than 5.
test_cases = [
    (15, 12), 
    (12, 8),   
    (10, 11),  
    (20, 6),   
    (4, 4)     
]

print(f"{'Pair':<10} | {'Condition Met?'}")
print("-" * 30)

for v1, v2 in test_cases:
   
    is_met = (v1 > 10 and v2 > 10) and (v1 > 5 or v2 > 5)
   
    result = "Yes" if is_met else "No"
    print(f"({v1}, {v2}):<10 | {result}")



16. Write a program to check voting eligibility (age >= 18).
    age=int(input ("enter your age:"))
    if age>18:
        print("You are eligible to vote")
    elif age==18:
        print("Congrats! You are eligible to vote from this year")
    else:
        print("SSorry! You can't vote")
        
SECTION E – ASSIGNMENT OPERATORS

17. Initialize a variable x = 10 and apply: x += 5 x -= 3 x *= 2 x /= 4
    Print value after each operation.
    x=10
    x += 5 
    print(x)  #--->15
    x -= 3
    print(x)  #--->7
    x *= 2 
    print(x)  #--->20
    x /= 4
    print(x)  #--->2.5
    

SECTION F – BITWISE OPERATORS

18. Find the output: print(5 & 3) print(5 | 3) print(5 ^ 3)
     print(5 & 3)  #-->1
     print(5 | 3)  #-->7
     print(5 ^ 3)  #-->6
 

19. Convert 6 and 3 into binary and perform: AND'&' OR XOR '|'
    a=6
    b=3
    
    print(f'6 in binary:{bin(a)}')
    print(f'3 in binary:{bin(b)}')
    print(f'AND & :{a&b}(binary: {bin(a & b)})')
    print(f'OR | :{a |b} (binary:{bin(a |b)})')
    print(f'XOR ^: {a ^ b} (binary:{bin(a ^ b)})')

SECTION G – IDENTITY & MEMBERSHIP OPERATORS

20. Predict the output: a = [1,2,3] b = a c = [1,2,3]print(a is b)print(a is c)
print(2 in a) print(5 not in a)

    a = [1,2,3]
    b = a 
    c = [1,2,3]
    print(a is b) #--->True
    print(a is c) #-->False
    print(2 in a) #-->True
    print(5 not in a)#-->True
    