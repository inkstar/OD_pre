nums=[1,2,4,3,5,4,7,2]
dp=[1]*len(nums)
count=[1]*2100
maxx=0
for i in range(len(nums)):
    for j in range(i):
        if nums[j]<nums[i]:
            if dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
                count[i]=count[j]
            elif dp[j]+1==dp[i]:
                count[i]+=count[j]
            print(nums[i],dp[i],dp[j],count[i])            
for i in range(len(dp)):
    if dp[i]==max(dp):
        maxx=count[i]
print)

            