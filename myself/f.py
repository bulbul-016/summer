ab=input().split()
for i,v in enumerate (ab):
    a=int(ab[0])
    b=int(ab[1])
cnt=0

while a<b or a==b:
    a=a*3
    b=b*2
    cnt+=1
    if a>b:
        break

print(cnt)