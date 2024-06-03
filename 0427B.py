s=list(map(str,input()))
i=0
s1=''
while(s[i]==min(s[i:])):
    s1+=s[i]
    i+=1
if s[i]!=min(s[i:]):
    s1+=min(s[(i):])
flag=0
for j in s[(i+1):]:
    if j==min(s[(i-1):]):
        flag=1
        s1+=s[i]
        continue
    if (j!=min(s[(i-1):]) and flag==0) or flag==1:
        s1+=j
print(s1)
    