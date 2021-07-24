number=int(input())
divisors=set()
summ=0
for i in range(1,number):
    if number%i==0:
        divisors.add(i)
for j in divisors:
    summ+=j
if summ==number:
    print("PERFECT")
else:
    print("NOT PERFECT")