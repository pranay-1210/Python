'''
Data Types in Python refers to the different types of data that can be stored in a variable.

There are for major categories of data types:

1. Numeric Data Types
2. Sequence Data Types
3. Set Data Types
4. Dictionary Data Types

In Numeric Data Types, we have:

1. int
2. float
3. complex
4. bool

In Sequence Data Types, we have:

1. list
2. tuple
3. String

'''
import sys;
x = 101
print(type(x)) # <class 'int'>
print(sys.getsizeof(x)) # Printing the size of the variable
print(id(x))
x = 202
print(id(x)) # Referring to the other memory location means it is a different variable

y = 10.1
print(type(y)) # <class 'float'>

z = 3+1j
print(type(z)) # <class 'complex'>

c3 = complex(3,4)
print(c3) # (3+4j)

a = True
print(type(a)) # <class 'bool'>

b = False
print(type(b)) # <class 'bool'>