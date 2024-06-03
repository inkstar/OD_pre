scores=[4,5,6,5]
ages=[2,1,2,1]

s=sorted(zip(scores,ages),key=lambda x:(x[0],x[1]))
from bisect import bisect_left
dp=[]
for i in range(len(s)):
    x=s[i][0]
    j= bisect_left(dp,x)
    if j==len(dp):
        dp.append(x)
    else:
        dp[j]=x

print(sum(dp))


