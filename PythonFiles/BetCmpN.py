# Beta comparison normal approximation
# psi_1 ~ Beta(a, b)(t)
# pi ~ Beta(theta, ro)(t)

import math
# Get user input
print("psi ~ Beta(a,b)")
print("Enter a")
a = float(input("a: "))
print("Enter b")
b = float(input("b: "))
print("pi ~ Beta(theta,ro)")
print("Enter theta")
theta = float(input("theta: "))
print("Enter ro")
ro = float(input("ro: "))
# Calculate standard deviation
sigma_psi = math.sqrt(a*b/((a+b)**2*(a+b+1)))
# Calculate expected value
mu_psi = a/(a+b)
# Calculate standard deviation
sigma_pi = math.sqrt(theta*ro/((theta+ro)**2*(theta+ro+1)))
# Calculate expected value
mu_pi = theta/(theta+ro)
# Calculate mu comparison
mu_z = mu_psi - mu_pi
# calculate standard deviation comparison
sigma_z =  math.sqrt(sigma_psi**2 + sigma_pi**2)

# Print results
print("sigma_psi = ")
print(sigma_psi)
print("mu_psi = ")
print(mu_psi)
print("sigma_pi = ")
print(sigma_pi)
print("mu_pi = ")
print(mu_pi)
print("mu_z = ")
print(mu_z)
print("sigma_z = ")
print(sigma_z)