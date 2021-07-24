import re

txt=input()
word=input()

x=re.search(word, txt)

if x:
    print(f"First time {word} occurred in position: {x.start()}")
else:
    print("Not found")