
dic={')':'(',']':'[','}':'{'}
stack=[]
s=list(input())             #输入字符串的同时存储于列表内部

depth=0                     #记录栈的深度
for i in s:
    if i in dic and stack:
        if stack[-1]==dic[i]:
            depth=max(depth,len(stack))
            stack.pop()
    else:
        stack.append(i)
if not stack:               #栈为空，说明全部匹配，则输出深度
    print(depth)
else:                       #栈不为空，说明部分匹配，输出0,表示不能完全匹配
    print('0')

