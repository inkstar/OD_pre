coins=[1,2,5]
amount=5
dp=[0]*(amount+1)
dp[0]=1
for x,coin in enumerate(coins):
    for i in range(coin,amount+1):
        dp[i]=dp[i]+dp[i-coin]
print(dp[amount])
