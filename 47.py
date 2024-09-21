sentence = input("enter sentence").strip().split(" ")
word = input("enter word")
print("word "+word+" is in the sentence" if word in sentence else "word "+word+"is not in the sentence")