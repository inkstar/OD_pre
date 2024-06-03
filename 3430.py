books=list(map(int,input().split(',')))
L=[]
W=[]
for i in range(0,len(books),2):
    L.append(books[i])
    W.append(books[i+1])
s=sorted(zip(L,W),key=lambda x:(x[0],-x[1]))
from bisect import bisect_left
dp=[]
for i in range(len(s)):
    x=s[i][1]
    j= bisect_left(dp,x)
    if j==len(dp):
        dp.append(x)
    else:
        dp[j]=x

print(len(dp))


