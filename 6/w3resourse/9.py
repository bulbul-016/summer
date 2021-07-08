number=int(input())

def f(NUMBER):
    cnt=0
    for i in range(2,NUMBER):
        if NUMBER%i==0:
            cnt+=1
    if cnt==0:
        return True
    else:
        return False
if f(number):
    print("PRIME")
else: 
    print("NOT PRIME")