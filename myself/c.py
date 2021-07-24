n=int(input())
nums=input().split()
lisst=list()
cnt=0
for i,v in enumerate (nums):
    lisst.append(nums[i])

for j,val in enumerate (lisst):
    for k,value in enumerate (lisst):
        if j>k:
            if lisst[j]==lisst[k]:
                cnt+=1
if cnt==0:
    print("YES")
else:
    print("NO")
            