txt=input().split()
lisst=list()
dictt=dict()
uzyn=0

for i,v in enumerate (txt):
    lisst.append(v)

for i in range(len(lisst)):
    dictt[len(lisst[i])]=(lisst[i])

for i in dictt:
    if i>uzyn:
        uzyn=i

print(dictt[uzyn])
print(uzyn)