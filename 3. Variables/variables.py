'''

What are Variables?

Variables are names assigned to data stored in a program.
They allow easy access and manipulation of data within the program.

Example:

length = 15 — Here, length is the variable name, and 15 is the data.
Variables can store either a single value (scalar) or multiple values (vectors/lists).

Memory Allocation:

Variables are stored in the computer's RAM during program execution.
Memory is allocated for the data the variable holds.
Variable names can be visualized as references (or pointers) to memory locations containing the data.
Multiple variables can refer to the same memory location if they hold the same immutable value.

Example:

If a = b = c = 111, all three variables point to the same data location.

Rules for Variable Naming:

1. Meaningful Variable Names

Variable names should clearly indicate the data they hold.
Short forms are acceptable, but unclear names like a, b, c should be avoided.

2. Allowed Characters in Variable Names

Variable names can contain alphabets (a–z, A–Z), numbers (0–9), and underscore (_).

3. Variable Naming Rules

Must start with a letter or underscore (_).
Cannot start with a number.
Numbers are allowed after the first character.
Variables can start with an underscore.

4. Keywords (Reserved Words)

Python keywords cannot be used as variable names.
Using a keyword as a variable name causes a syntax error.

5. Case Sensitivity

Python variable names are case sensitive.
price, Price, and PRICE are treated as different variables.

'''

length = 15
print(length) # 15 

prices = [0,20,30,40,50]
print(prices) # [0, 20, 30, 40, 50]

name,price,quantity = 'pen',10,5 #multiple declaration
print(name,price,quantity) # pen 10 5

a=b=c=1
print(a,b,c) # 1 1 1

a=20
print(type(a)) # <class 'int'>