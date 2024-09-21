number =  (int(input("enter number")),int(input("enter number")))
factors = [(list(i for i in range(1,number[0]//2+1) if number[0]%i==0)),(list(i for i in range(1,number[1]//2+1) if number[1]%i == 0))]
if number[0]==number[1]:
    factors[0].append(number[0])
    factors[1].append(number[0])
hcf=(max([i for i in factors[0] if i in factors[1]]))
print("lcm is ", (number[1]*number[0])//hcf)