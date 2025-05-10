# Student deviation Z = X +- Y
# X ~ t(mu_x, sigma_x, v_x)
# Y ~ t(mu_y, sigma_y, v_y)

import math

# Get user input
print("Enter mean of X")
mu_x = float(input("mu_x: "))
print("Enter mean of Y")
mu_y = float(input("mu_y: "))
print("Enter stand dev of X")
sigma_x = float(input("sigma_x: "))
print("Enter stand dev of Y")
sigma_y = float(input("sigma_y: "))
print("Enter deg free of X")
v_x = int(input("v_x: "))
print("Enter deg free of Y")
v_y = int(input("v_y: "))

# Choose operation: Addition or Subtraction
print("Choose operation")
print("'+' for Z = X + Y")
print("'-' for Z = X - Y")
operation = input("Operator: ").strip()

if operation == "+":
    mu_z = mu_x + mu_y
elif operation == "-":
    mu_z = mu_x - mu_y
else:
    print("Invalid operation! Please enter '+' or '-'.")
    exit()

# Calculate standard deviation
sigma_z = math.sqrt(sigma_x**2 + sigma_y**2)

# Compute degrees of freedom using Welch-Satterthwaite equation
numerator = ((sigma_x**2) / (v_x + 1) + (sigma_y**2) / (v_y + 1)) ** 2
denominator = (((sigma_x**2) / (v_x + 1))**2) / v_x + (((sigma_y**2) / (v_y + 1))**2) / v_y
v_z = math.floor(numerator / denominator) if denominator > 0 else float('inf')

# Print results
#print(f"Mean of Z: {mu_z}")
#print(f"Standard deviation of Z: {sigma_z}")
#print(f"Degrees of freedom of Z: {v_z}")
print("mu_z = ")
print(mu_z)
print("sigma_z = ")
print(sigma_z)
print("v_z = ")
print(v_z)
