# pweib
#
# Weibull CDF calculator
# T ~ W(k,lambda)(t)
import math
while True:
    print("T ~ W(k,lambda)(t)")
    print("Enter t")
    t = float(input("t: "))
    print("Enter k")
    k = float(input("k: "))
    print("Enter lambda")
    l = float(input("lambda: "))
    W = 1-math.exp(-(t / l) ** k)
    print("Weibull CDF =")
    print(W)
    # Ask the user if they want to try again
    print("Run again?")
    again = input("1=yes, 0=no:").strip().lower()
    if again != "1":
        print("Goodbye!")
        break   