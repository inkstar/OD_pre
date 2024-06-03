s1=input()
s=list(s1)
i=0
stack=[]
flag=[o,0,0,0,0]t=リu
while i<len(s):if s[i]=='<' and len(stack)>=1:stack.pop()else:

if s[i]!='<':
stack.append(s[i])if 'A'<=s[i]<='Z': flag[1]=1elif 'a'<=s[i]<='z': flag[2]=1elif '0'<=s[i]<='9': flag[3]=1elif s[i]!='' and s[i]!='<': flag[4]=1
i+=1
if sum(flag)=4 and len(stack)>=8:

t+=',truel

else:

t+=',false 

ans=''.join(stack)+t

print(ans)