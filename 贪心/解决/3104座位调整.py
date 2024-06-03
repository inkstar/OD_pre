desk=list(map(int,input().split(',')))
ans=0
n=len(desk)
if n==1 and desk[0]==-:
    ans=1
else:
    for i,x in enumerate(desk):
        if i==0 and n>=2 and desk[0]==0 and desk[1]==0:
            desk[0]+=1
            ans+=1
        elif i==n-1 and n>=2 and desk[-2]==0 and desk[-1]==0:
            desk[-1]+=1
            ans+=1
        elif i+1<=n-1 and i-1>=0 and desk[i-1]==0 and desk[i+1]==0 and desk[i]==0:
            desk[i]+=1
            ans+=1
print(ans)
