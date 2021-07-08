given=input().split(", ")
result=[]
for i in given:
    if int(i)%2==0:
        result+=i
print(result)