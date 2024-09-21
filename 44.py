stringing = input("enter name").strip().split(" ")
print(''.join([stringing[i][0].upper()+"." for i in range(len(stringing)-1)])+stringing[-1])