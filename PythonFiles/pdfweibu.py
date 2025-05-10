#dweib
#
# Weibull pdf calculator
# T ~ w(k,lambda)(t)
import math
while True:
    print("T~w(k,lambda)(t)")
    print("Enter t")
    t = float(input("t: "))
    print("Enter k")
    k = float(input("k: "))
    print("Enter lambda")
    l = float(input("lambda: "))
    w = (k / l) * ((t / l) ** (k - 1)) * math.exp(-((t / l) ** k))
    print("Weibull pdf =")
    print(w)
    
    # Ask the user if they want to try again
    print("Run again?")
    again = input("1=yes, 0=no:").strip().lower()
    if again != "1":
        print("Goodbye!")
        break   