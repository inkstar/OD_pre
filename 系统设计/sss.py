s=list(map(int,input().split(',')))
ans=0
def ishigher(s:list,k:int):
    if len(s)==1 and s[k]>0:return 1
    elif len(s)>1:
        if k==0 and s[k]>s[k+1]:return 1
        elif k==len(s)-1 and s[k]>s[k-1]:return 1
        elif s[k]>s[k-1] and s[k]>s[k+1]:return 1
    else:
        return 0
for i in range(len(s)):
    ans+=ishigher(s,i)
print(ans)