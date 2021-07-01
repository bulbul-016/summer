nums=list[int(input())]
cnt=0
for i in range(len(nums)-1):
    for j in range(len(nums)):
        if i<j:
            if nums[i]==nums[j]:
                cnt+=1
print(cnt)