# =========================
# 1) Variables and Data Types - 10 examples
# =========================
a = 10                      # int
b = -45                     # int
c = 3.14                    # float
d = -0.99                   # float
e = "Hello"                 # str
f = 'A'                     # str
g = True                    # bool
h = False                   # bool
i = 2 + 3j                  # complex
j = complex(5, -2)          # complex


# =========================
# 2) Keywords and Identifiers - 10 examples
# =========================
# Valid identifiers
student_name = "Ravi"       # valid
_marks = 95                 # valid
age2 = 20                   # valid
TOTAL = 500                 # valid
myVar = "ok"                # valid

# Invalid identifiers (examples as strings to avoid error)
invalid1 = "2name"          # starts with number (invalid)
invalid2 = "my-name"        # hyphen not allowed (invalid)
invalid3 = "class"          # keyword, cannot be identifier
invalid4 = "def"            # keyword, cannot be identifier
invalid5 = "first name"     # space not allowed (invalid)


# =========================
# 3) Input and Output Functions - 10 examples
# =========================
name = input("Enter name: ")
print("Hello,", name)

age = int(input("Enter age: "))
print("Age:", age)

price = float(input("Enter price: "))
print("Price is", price)

x = input("Enter first value: ")
y = input("Enter second value: ")
print("You entered:", x, y)

city = input("City: ")
print(f"Welcome to {city}")

num = int(input("Enter number: "))
print("Square =", num * num)

print("A", "B", "C", sep="-")
print("Line1\nLine2")
print("Python", end=" ")
print("Programming")


# =========================
# 4) Arithmetic Operators - 10 examples
# =========================
print(10 + 3)   # +
print(10 - 3)   # -
print(10 * 3)   # *
print(10 / 3)   # /
print(10 // 3)  # //
print(10 % 3)   # %
print(2 ** 4)   # **
print((5 + 2) * 3)
print(abs(-12))
print(round(5.678, 2))


# =========================
# 5) Relational Operators - 10 examples
# =========================
print(5 == 5)   # ==
print(5 != 3)   # !=
print(7 > 2)    # >
print(2 < 7)    # <
print(8 >= 8)   # >=
print(6 <= 9)   # <=
print("a" == "A")
print(10 > 20)
print(15 <= 15)
print(4 != 4)


# =========================
# 6) Logical Operators - 10 examples
# =========================
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
print(not False)
print((5 > 2) and (8 > 3))
print((5 > 2) and (8 < 3))
print((5 < 2) or (8 > 3))
print(not (10 == 10))


# =========================
# 7) Assignment Operators - 10 examples
# =========================
x = 10        # =
x += 5        # +=
x -= 3        # -=
x *= 2        # *=
x /= 4        # /=
x //= 2       # //=
x %= 3        # %=
x **= 2       # **=
x &= 7        # &=
x |= 2        # |=


# =========================
# 8) Bitwise Operators - 10 examples
# =========================
print(5 & 3)    # AND
print(5 | 3)    # OR
print(5 ^ 3)    # XOR
print(~5)       # NOT
print(5 << 1)   # left shift
print(5 >> 1)   # right shift
print(12 & 10)
print(12 | 10)
print(12 ^ 10)
print(8 >> 2)


# =========================
# 9) Identity and Membership Operators - 10 examples
# =========================
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)            # identity
print(a is c)
print(a is not c)
print(a == c)

text = "python"
nums = [10, 20, 30]

print("p" in text)       # membership
print("z" in text)
print(20 in nums)
print(40 not in nums)
print("th" in text)
