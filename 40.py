listing = list(input("enter number").strip().split(" "))
even = [i for i in listing if int(i)%2==0]
odd = [i for i in listing if int(i)%2!=0]
print(listing,"\n even :", even, "\n odd :",odd)