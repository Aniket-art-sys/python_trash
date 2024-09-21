number = int(input("enter number"))
print("".join([" "*(number-_-1)+"".join([str(i) for i in range(1,_+1)][::1])+''.join([str(i) for i in range(1,_+2)][::-1])+"\n" for _ in range(number)]))