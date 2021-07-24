strr=input()
reverse=""
res=list(reversed(strr))
for i in res:
    reverse+=i


def f(strrrr, res):
    if strrrr==res:
        print("PALINDROME")
    else:
        print("NOT PALINDROME")

f(strr, reverse)