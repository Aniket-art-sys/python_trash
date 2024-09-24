choice = 0
sentence =input("enter sentence")
key = input("enter key")
def breaker (string):
    return [ord(i) for i in string]
def joiner (list):
    return  "".join([chr(i) for i in list])
def xorer (sentence_l,key_l):
    return  [sentence_l[i]^key_l[i] for i in range(len(sentence_l))]
while True:
    choice = int(input("enter value"))
    if choice in [1,2]:
        break
if choice == 1:
    print("encrypt")
    print(xorer(breaker(sentence),breaker(key)))
if choice ==2:
    sentence = sentence.replace("[","").replace("]","").replace(",","").split(" ")
    sentence_ = [int(i) for i in sentence]
    print(joiner(xorer(sentence_,breaker(key))))

