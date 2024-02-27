stack,digit,res=[],0,""
s=input()
for i in s:
    if i=='}':
        stack.append([digit,res])
        digit,res=0,""
    elif i=='{' and stack:
        lastdigit,lastres=stack.pop()
        res=lastres+lastdigit*res
    elif '0'<=i<='9':
        digit=int(i)
        res=digit*res
        stack.append([1,res])
        res=""
    else:
        res+=i
print (''.join(stack))