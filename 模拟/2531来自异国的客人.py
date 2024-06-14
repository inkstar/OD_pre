k,n,m=map(int,input().split())

ans=0
tmp=0
for i in range(10,-1,-1):
    if k>=m**i:
        tmp=k//(m**i)
        if(tmp==n):
            ans+=1
        k=k-tmp*(m**i)
print(ans)
