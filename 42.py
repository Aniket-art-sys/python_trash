stringing= input("enter string").strip()
number = len(stringing)
print(''.join(" "*(number-i)+stringing[0:i+1]+"\n" for i in range(number)))