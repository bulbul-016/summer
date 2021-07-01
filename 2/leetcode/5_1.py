given=int(input())
plus=0
multi=1
for i, val in enumerate(given):
    plus+=int(val)
    multi*=int(val)
print(multi-plus)