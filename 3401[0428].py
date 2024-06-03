from collections import defaultdict
M,N,K=map(int,input().split())
L=set(map(int,input().split()))
dp=[defaultdict(int) for _ in range(N+2)]
dp[0]={M:1}

for i in range(N+2):
    for j in range(max(i-3,0),i):
        for rest_life in dp[j]:
            if i not in L:
                dp[i][rest_life]+=dp[j][rest_life]
            else:
                if rest_life-1>0:
                    dp[i][rest_life-1]+=dp[j][rest_life]
print(sum(dp[-1].values()))