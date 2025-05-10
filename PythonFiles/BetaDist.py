# Beta distribution
# pi ~ Beta(a, b)(t)

import math

# Get user input
print("Enter a")
a = float(input("a: "))
print("Enter b")
b = float(input("b: "))

# Calculate standard deviation
sigma_pi = math.sqrt(a*b/((a+b)**2*(a+b+1)))
# Calculate expected value
mu_pi = a/(a+b)
# Calculate pi max
pi_max = (a-1)/(a+b-2)
# Calculate median
pi_med = (a-1/3)/(a+b-2/3)


# Print results
print("sigma_pi = ")
print(sigma_pi)
print("mu_pi = ")
print(mu_pi)
print("pi_max = ")
print(pi_max)
print("pi_median = ")
print(pi_med)
