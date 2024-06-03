
envelopes=[[5,4],[6,4],[6,7],[2,3]]

s=sorted(envelopes,key=lambda x:(x[0],-x[1]))
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


