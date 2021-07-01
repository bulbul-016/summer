given=int(list[input().split()])
maximus=int(given[1])+int(given[2])
for i,val in enumerate(len(given)-1):
    for j, value in enumerate(len(given)):
        if i>j:
            if given[i]+given[j]>maximus:
                maximus=given[i]+given[j]
print(maximus)