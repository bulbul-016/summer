number=int(input())
factorial=1
if number==0:
    print(1)
else:
    for i in range(number):
        factorial*=i+1
    print(factorial)