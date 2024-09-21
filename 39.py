list=[]
while (True):
    choice = int(input("enter choice from :\n 1.append\n2.remove\n3.modify\n4.find\n5.display"))
    if choice==1:
        print(list,"append")
        list.append(input("enter value"))
    elif choice == 2:
        print(list,"remove")
        list.pop(int(input("enter index")))
    elif choice == 3:
        print(list,"modify")
        list[int(input("enter index"))]= input("enter value")
    elif choice == 4:
        print(list,"find")
        print(list.index(input("enter value")))
    elif choice == 5:
        print(list)
    else:
        print("not an option")