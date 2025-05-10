def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def binomial(x, y):
    return factorial(x) // (factorial(y) * factorial(x - y))

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input.")
            print("Enter an integer.")

while True:
    print("psi ~ Beta(a,b)")
    a = get_integer("Enter a: ")
    b = get_integer("Enter b: ")

    print("pi ~ Beta(theta,ro)")
    theta = get_integer("Enter theta: ")
    ro = get_integer("Enter ro: ")

    total_sum = 0
    for k in range(0, theta):
        numerator = binomial(a + b, a) * binomial(k + ro, k) * a * b * ro * (a + b + k + ro)
        denumerator = binomial(a + b + k + ro, a + k) * (a + b) * (k + ro) * (a + k) * (b + ro)
        total_sum += numerator / denumerator

    print("P(psi <= pi) = ")
    print(total_sum)
    print("Run again?")
    again = input("1=yes, 0=no:").strip().lower()
    if again != "1":
        print("Goodbye!")
        break
