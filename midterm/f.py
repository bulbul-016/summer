import re

username=input()
#password=input()

u=re.search("\w{3,32}#\d{4}", username)
#p=re.search("", password)

if u:
    print("Welcome to Discord")
else:
    print("Invalid password or username")