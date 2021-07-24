id=input().split()
cnt=int(input())
miss=list()
isid=list()

for i in id:
    isid.append(int(i))

for i in range(1, int(id[len(id)-1])+1):
    miss.append(i)

for i,v in enumerate (isid):
    for j,w in enumerate (miss):
        if miss[j]==isid[i]:
            miss.remove(miss[j])


print(miss[cnt-1])