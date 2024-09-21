number = int(input("enter number"))
ranger = int(input("enter n"))
print(sum(list(number**i for i in range(ranger+1))))