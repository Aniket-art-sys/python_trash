number = input('enter a number')
a= int(number)
print("its a palindromic number" if number[::-1] == number else "its an non palindromic  number")