number = int(input("enter number"))
prime_factorial =[]
while number>1:
    for i in range(2,int(number)+1):
        if number%i == 0:
            number=number/i
            prime_factorial.append(i)
print(prime_factorial)
print(sum(prime_factorial))