number =  (int(input("enter first number")),int(input("enter second number")))
if (sum(list(i for i in range(1,number[1]//2+1) if number[1]%i==0)))==number[0] and number[1]==(sum(list(i for i in range(1,number[0]//2+1) if number[0]%i==0))):
    print("it's a amicable number")
else:
    print("it's not a amicable number")