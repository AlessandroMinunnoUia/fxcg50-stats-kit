# Gamma distribution
# pi ~ gamma(k, l)(t)

import math

# Get user input
print("Enter k")
a = float(input("a: "))
print("Enter l")
b = float(input("b: "))

# Calculate standard deviation
sigma = a/b**2
# Calculate expected value
mu = a/b
# Calculate T_max
T_max = (a-1)/b

# Print results
print("sigma = ")
print(sigma)
print("mu = ")
print(mu)
print("pi_max = ")
print(T_max)

