while (True):
    try:
        amount = int(input("enter amount"))
        break
    except:
        print("enter a number")
notes = (2000, 500, 200, 100, 50, 20, 10, 5, 1)
notesno = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 9):
    if amount % notes[i]!=0:
        notesno[i] = amount // notes[i]
        if amount // notes[i]>0:
            amount-=(notes[i]*notesno[i])
    else:
        notesno[i]=amount//notes[i]
        break
#print("numbers of ", (notes[_] for _ in range(0, 9)), " needed are ", (notesno[_] for _ in range(0, 9)))
for i in range(0, 9):
    print("number of notes of ",notes[i]," needed are :",notesno[i])