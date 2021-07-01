nums=input().split()
mini=int(nums[0])
for i,val in enumerate(nums):
    if int(val)>0 and int(val)<int(mini):
        mini=val
print(mini)