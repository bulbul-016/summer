command=str(input())
listt=[]
result=''
for i in command:
    listt.append(i)
for j in range(len(listt)):
    if listt[j]=='G':
        result+='G'
    elif listt[j]=='(' and listt[j+1]==')':
        result+='o'
    elif listt[j]=='(' and listt[j+1]=='a':
        result+='al'
print(result)

'''
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command
'''