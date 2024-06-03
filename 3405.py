m,n=map(int,input().split())
dp=[[[0]*(n+1) for _ in range(n-m+2)] for i in range(m+1)]
for j in range(1,n//m+1):
    dp[1][j][j]=1

for i in range(1,m):
    for j in range(1,n-m+2):
        for k in range(i,n+1):
            for d in range(0,4):
                if j+d<=n-m+1 and j+k+d<=n:
                    dp[i+1][j+d][k+j+d]+=dp[i][j][k]

ans=0
for j in range(n-m+2):
    ans+=dp[m][j][n]
print(ans) 