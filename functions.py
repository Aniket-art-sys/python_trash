import random
def split (limit, pr, ranlim):
    nums=[i for i in range(0,limit)]
    likey = [0 for i in range(0,limit)]
    likey.append(pr)
    random.shuffle(nums)
    for i in nums:
        rand=random.randrange((likey[limit]//ranlim))
        likey[i]=rand
        likey[limit]-= rand
    likey[nums[limit-1]] += likey[limit]
    likey.pop(limit)
    return likey
def choice (list,lastmoves):
    listing = [0]*list[0] + [1]*list[1] + [2]*list[2]
    if lastmoves[len(lastmoves)-1] == lastmoves[len(lastmoves)-2] and listing[lastmoves[len(lastmoves)-1]]>21:
        for i in range(listing.count(lastmoves[len(lastmoves-1)])-10):
            try:
                listing.remove(lastmoves[len(lastmoves)-1])
            except:
                break
    return listing[random.randrange(len(listing))]
def data_in (cm,pm,rl):
    listing = data_out()
    for i in range(1):
        if rl == "lost" :
            a = [0, 1, 2]
            a.pop(cm)
            for i in a:
                if listing[0] >10 and listing[1] > 10 and listing[2] > 10 and listing[cm]> 11 :
                    listing[cm] += 1
                    listing[i]-=1
                else:
                    a=[0,1,2]
                    a.pop(listing.index(10))
                    listing[listing.index(10)] = 12
                    if listing[a[0]]>listing[a[1]]:
                        listing[a[0]]-=2
                    else:
                        listing[a[0]]<listing[a[1]]
                        listing[a[1]]-=2

        elif rl == "win" :
            a=[0,1,2]
            a.pop(cm)
            for i in a:
                if listing[0] > 10 and listing[1] > 10 and listing[2] > 10 and listing[cm] > 11:
                    listing[cm] -= 1
                    listing[i]+=1
    f = open("data.txt","w")
    f.write(str(listing[0])+" "+str(listing[1])+" "+str(listing[2]))
    f.close()

def data_out ():
    f = open("data.txt","r")
    data = f.readline().strip().split(" ")
    f.close()
    for i in range(3):
        data[i]=int(data[i])
    return data


def export_data (tuple_info):
    f = open("pastgames.txt", "a")
    f.write(tuple_info+"\n")
    f.close()
def import_data (name):
    f = open(name, "r")
    nlist =[]
    for i in f:
        twrp = f.readline().strip().split(" ")
        nlist.append(tuple(twrp))
    nlist.pop()
    f.close()
    return nlist
def create_nes ():
    f = open("data.txt","w")
    f.write("33 33 34")
    f.close()
    f = open("pastgames.txt","w")
    f.close()
