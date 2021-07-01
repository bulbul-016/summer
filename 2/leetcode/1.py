address=input()
result=''
for i in address:
    if i!='.':
        result+=i
    else: result+='[.]'
print(result)

'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
'''