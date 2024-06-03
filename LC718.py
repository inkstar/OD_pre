text1 = "abcde"
text2 = "ace"
nums1=list(text1)
nums2=list(text2)
maxx=0
m=len(nums1)
n=len(nums2)

dp=[[0]*(n+2) for _ in range(m+2)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if nums1[i-1]==nums2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            maxx=max(maxx,dp[i][j])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])


print(maxx)