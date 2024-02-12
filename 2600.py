
dic={')':'(',']':'[','}':'{'}
stack=[]
s=list(input())
flag=1
depth=0
for i in s:
    if i in dic and stack:
        if stack[-1]==dic[i]:
            depth=max(depth,len(stack))
            stack.pop()
        else :
            flag=False
    else:
        stack.append(i)
if not stack:
    print(depth)
else:
    print('0')

