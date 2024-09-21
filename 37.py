number = int(input("enter number"))
print("".join([" "*(number-i-1)+"*"*(range(1,number*2,2)[i] )+"\n" for i in range(number)]))