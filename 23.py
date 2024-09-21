number =input("enter number").strip()
print("it's an armstrong number" if sum(list(int(i)**3 for i in number))==int(number) else "it's not an armstrong number")
print(sum(list(int(i)**3 for i in number)))