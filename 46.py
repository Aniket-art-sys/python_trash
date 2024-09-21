stringing = input("enter sentence").strip().split(" ")
print(''.join(stringing[i][::-1] + " " for i in range(len(stringing))))