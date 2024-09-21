stringing= input("enter string").strip()
number = len(stringing)
print(''.join(stringing[0:i+1]+"\n" for i in range(number)))