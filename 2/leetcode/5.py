number=int(input())
plus=0
multi=1
while(number!=0):
    plus=plus+(number%10)
    multi=multi*(number%10)
    number=number//10
print(multi-plus)