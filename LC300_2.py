
from bisect import bisect_left
dp=[]
nums = [10,9,2,5,3,7,101,18]
for x in nums:
    j = bisect_left(dp,x)
    if j==len(dp):dp.append(x)
    else:
        dp[j]=x
return len(dp)     