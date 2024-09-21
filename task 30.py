while(True):
    try:
        number =str(input("enter number"))
        break
    except :
        print("enter a number")
print(number[::-1])