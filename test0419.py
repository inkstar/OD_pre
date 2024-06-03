from collections import defaultdict
N=16
dp = [defaultdict(int) for _ in range(N+2)]
dp[6]=6
dp[0] = {M: 1}
print(dp)