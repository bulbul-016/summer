nums=input().split()
mylist=[]
for i,v in enumerate(nums):
    if int(nums[i])%2==0:
        mylist.append(v)
print(mylist)