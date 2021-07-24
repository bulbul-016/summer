nums=input().split()
lisst=list()
cnt=0

def f(v):
    dnt=len(v)
    if dnt%2==0:
        return True
    elif dnt%2==1: 
        return False


for i in range(len(nums)):
    lisst.append(nums[i])

for j,v in enumerate (lisst):
    if f(v):
        cnt+=1
print(cnt)