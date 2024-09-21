number =  int(input("enter number"))
if number==(sum(list(i for i in range(1,number//2+1) if number%i==0))):
    print("it's a perfect number")
else:
    print("it's not a perfect number")