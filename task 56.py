import random
number = random.randrange(0,7 )
for i in range(3,0,-1):
    while(True):
        try:
            guess = int(input("enter ur guess"))
            if(guess>0 or guess<6):
                break
            else:print("enter number between 0-6")
        except:
            print("enter a number!0-6")
    if guess> number :
        print("ur guess is larger! tries left : ",i)
    if guess< number :
        print("ur guess is smaller! tries left : ",i)
    if guess==number :
        print("ur guess is correct! tries used : ",i)
        break
print("u ran out of tries")


