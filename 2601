s=input().split()
sum=0
stack=[]
for i in s:
    if i.isnumeric():
        sum+=int(i)
        stack.append(int(i))
    elif i.startswith('-') and i[1:].isnumeric():
        sum-=int(i[1:])
        j=-int(i[1:])
        stack.append(j)
    elif i=='+' and len(stack)>=2:
        j=stack[-1]+stack[-2]
        stack.append(j)
        sum+=j
    elif i=='D' and stack:
        j=stack[-1]*2
        stack.append(j)
        sum+=j
    elif i=='C' and stack:
        j=0
        sum-=stack[-1]
        stack.pop()
        #stack.append(j)
    else:
        sum=-1
        break
print(sum)
#print(stack)