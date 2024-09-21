countryies = input("enter name of 10 counties ").strip().split(" ")
while len(countryies)<10:
    print("enter more name ",countryies)
    countryies += input().strip().strip(" ")
print(''.join([i +" " for i in countryies if len(i)>6]))