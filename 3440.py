text1=input()
text2=input()
s1=list(text1)
s2=list(text2)
m=len(text1)
n=len(text2)
ans=''
maxx=0
dp=[[0]*(m+1)  for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s2[i-1]==s1[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            if maxx<dp[i][j]:
                maxx=dp[i][j]
                ans=text2[i-maxx:i]
print(ans)

