a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
if sum%2==1:
    print((sum+1)//2)
else: print(sum//2)