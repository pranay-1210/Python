# Program to calculate the surface area of a cuboid

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
surface_area = 2 * (length * width + length * height + width * height)
print("Surface area is: ",surface_area)