from urllib.error import URLError

print("stone,paper,sizer")
import random
import urllib.request
import os
for i in range(3):
    if not os.path.exists("data.txt"):
        print("making data file")
        f = open("data.txt", "w")
        f.write("33 33 34")
        f.close()
    elif not os.path.exists("pastgames.txt"):
        print("making game record file")
        f = open("pastgames.txt", "w")
        f.close()
    elif not  os.path.exists("functions.py"):
        print("downloading additional files")
        truee =True
        while truee:
            try:
                urllib.request.urlretrieve("https://raw.githubusercontent.com/Aniket-art-sys/python_trash/main/functions.py","functions.py")
                print("download complete!")
                break
            except URLError:
                print("no data connection\nRetry? y or n")
                while True:
                    if input()=="n":
                            print("can't work without it")
                            exit()
                    elif input() =="y":
                        break
                    else:
                        print("enter n or y ")
import functions
cb = functions.split(3,100,1)
last_moves =[0,0]
while(True):
    computer_choices = functions.choice(functions.data_out(),last_moves)
    last_moves.append(computer_choices)
    true =True
    while(true):
        try:
            pc_choice =input("enter stone paper or sizer : ")
            for i in ["stone","paper","sizer"]:
                if i == pc_choice:
                    true=False
        except:
            print("enter stone paper or sizer")
    true=True
    while(true):
        if pc_choice == ["stone","paper","sizer"][computer_choices]:
            print("tie")
            functions.export_data(["stone","paper","sizer"][computer_choices] +" " +["stone","paper","sizer"][computer_choices]+" "+"tie")
            break
        for a, b, c in [("stone","paper","lost"),("stone","sizer","win"),("sizer","paper","win"),("sizer","stone","lost"),("paper","sizer","lost"),("paper","stone","win")]:
            if ["stone","paper","sizer"][computer_choices]==b and pc_choice ==a:
                print("you ",c," their choice was ", b)
                functions.export_data(str(a)+" "+str(b)+" "+str(c))
                functions.data_in(("stone","paper","sizer").index(b),a,c)
                true=False
            else:
                true = False


