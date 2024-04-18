s=input().split(',')
flag=0
maxx=0
cnt=0
ans=0
for i in range(len(s)):
    if s[i]=='0':
        cnt+=1
        if i==len(s)-1:
            ans=cnt
            maxx=max(maxx,ans)
    elif s[i]=='1':
        if flag==0 and i!=0:
            ans=cnt-1
            maxx=max(maxx,ans)
        flag=1
        ans=int(cnt/2+0.5)
        maxx=max(maxx,ans)
        cnt=0

print(maxx)

