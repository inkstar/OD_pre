D=eval(input())
N=eval(input())
from math import inf
ls=[]
ls=[[0,0]]
for _ in range(N):
    dis,time = map(int,input().split())
    ls.append([dis,time+1])
ls.append([D,0])
dp=[inf]*(N+2)
dp[0]=0
for i in range(len(ls)):
    for j in range(i-1,-1,-1):
        if ls[i][0]-ls[j][0]>1000:
            break
        else:
            dp[i]=min(dp[j]+ls[i][1],dp[i])
print(dp[-1]+D//100)