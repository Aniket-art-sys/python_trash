number = int(input("enter number"))
ranger = int(input("enter n"))
def factorial(number):
    fac = 1
    for i in range(1, number):
        fac *= i
    return fac
print(sum(list(number ** (i * 2) / factorial(i * 2) for i in range(0,ranger + 1,2))))
