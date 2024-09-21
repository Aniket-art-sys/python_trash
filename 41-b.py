number =int(input("enter number"))
print(''.join([str(" "*(number-i))+str("*"*i)+str("*"*(i-1))+"\n" for i in range(number+1)]))