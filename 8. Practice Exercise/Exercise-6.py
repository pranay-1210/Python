# Program to calculate the displacement

initial_velocity = float(input("Enter the initial velocity: "))
acceleration = float(input("Enter the acceleration: "))
time = float(input("Enter the time: "))
displacement = initial_velocity * time + 0.5 * acceleration * time * time
print("Displacement is: ",displacement)