s=input()
safety_num=[0,0,0,0]
stack=[]
flag=''
for i in s:
    if stack and i=='<':
        stack.pop()
    elif not stack and i=='<':
        continue
    elif i!='<':
        stack.append(i)
for i in stack:
    if 'a'<=i<='z':
        safety_num[0]=1
    elif '0'<=i<='9':
        safety_num[1]=1
    elif 'A'<=i<='Z':
        safety_num[2]=1
    else:
        safety_num[3]=1
if sum(safety_num)==4 and len(stack)>=8:
    flag=',true'
else:
    flag=',false'
s2=''.join(stack)+flag
print(s2)
