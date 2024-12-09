# Casting is when you change an object data type to another data type.
# There are two types of casting:
# 1. Implicit Casting (done automatically).
# 2. Explicit Casting (done manually).

# Implicit Casting
x = 10
y = 20.5
z = x + y
print(z)  # Output: 30.5

# Explicit Casting
x = 10
print(type(x))  # Output: <class 'int'>
y = str(x)
print(y) # Output: 10
print(type(y))  # Output: <class 'str'>


