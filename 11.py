numbers = [int(input("How many?")),1,1]
for i in range (numbers[0]):
    numbers.append(numbers[-1] + numbers[-2])
print(numbers[1:])