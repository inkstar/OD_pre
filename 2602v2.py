s=input()
stack=[]
num=0
for i,ch in enumerate(s):
    if ch =='{' or ch.isalpha():
        stack.append(ch)
    elif ch.isnumeric():
        num=num*10+int(ch)
        if i==len(s)-1 or not s[i+1].isnumeric():
            stack[-1]*=num
            num=0
    elif ch=='}':
        str_in_bracket=""
        while(stack[-1]!='{'):
            str_in_bracket=stack.pop()+str_in_bracket
        stack.pop()
        stack.append(str_in_bracket)
print(''.join(stack))
