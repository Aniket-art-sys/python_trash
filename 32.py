number = int(input("enter number"))
ranger = int(input("enter n"))
def factorial (number):
    fac = 1
    for i in range(1,number):
        fac*=i
    return fac
print(sum(list(number**i/factorial(i) for i in range(ranger+1))))