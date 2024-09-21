number = int(input("enter nunber"))
print(''.join([f"{number} x {i} = {number * i}\n" for i in range(1, 11)]))