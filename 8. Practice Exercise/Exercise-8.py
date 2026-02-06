# Program to find the roots of a quadratic equation

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

d = (b*b) - (4*a*c)
root1 = (-b + d**(1/2)) / (2*a)
root2 = (-b - d**(1/2)) / (2*a)
print("Root 1 is: ",root1)
print("Root 2 is: ",root2)