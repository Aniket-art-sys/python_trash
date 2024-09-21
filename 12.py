number =  int(input("enter number"))
print(list(i for i in range(1,number//2+1) if number%i==0))