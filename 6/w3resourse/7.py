soz=input()
ulken=0
kishi=0
for i in soz:
    if i.isupper():
        ulken+=1
    elif i.islower():
        kishi+=1
print(f"UKKEN - {ulken}")
print(f"KSHI - {kishi}")