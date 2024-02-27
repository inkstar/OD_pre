sign=1
# s=input()
stack=[]
ans=0
i=0
while i<=len(s):
    j=s[i]
    if j==' ':
        i+=1
    elif j.isdigit():
        value=ord(j)-ord('0')
        while i+1<len(s) and s[i+1].isdigit():
            i=i+1
            value=value*10+ord(s[i])-ord('0')
        ans+=value*sign
        i+=1
    elif j=='+':
        sign=1
        i+=1
    elif j=='-':
        sign=-1
        i+=1
    elif j=='(':
        stack.append(ans)
        ans=0
        stack.append(sign)
        sign=1
        i+=1
    elif j==')':
        formersign = stack.pop()
        formerans =stack.pop()

        ans= formerans + formersign* ans
        i+=1



