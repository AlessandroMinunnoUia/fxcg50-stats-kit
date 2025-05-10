#qweib
#
# Weibull CDF calculator
# T ~ W^-1(k,lambda)(p)
import math
while True:
    print("T~W^-1(k,lambda)(p)")
    print("Enter p")
    p = float(input("p: "))
    print("Enter k")
    k = float(input("k: "))
    print("Enter lambda")
    l = float(input("lambda: "))
    q = l*(-math.log(1-p))**(1/k)
    print("Weibull iCDF =")
    print(q)
    # Ask the user if they want to try again
    print("Run again?")
    again = input("1=yes, 0=no:").strip().lower()
    if again != "1":
        print("Goodbye!")
        break   