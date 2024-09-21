while(True):
    try:
        number =str(input("enter number"))
        break
    except :
        print("enter a number")
if number== number[::-1]:
    print("it's a PALINDROMIC number")
