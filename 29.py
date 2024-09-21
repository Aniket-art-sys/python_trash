numbers_string=str(input("enter number"))
numbers=list(numbers_string.split(" "))
nums=[]
for i in numbers:
    if i.isdigit():
        nums.append(i)
print([nums.sort(),nums][1])
print([nums.sort(reverse=True),nums][1])