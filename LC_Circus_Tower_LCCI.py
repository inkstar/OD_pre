height = [8378,8535,8998,3766,648,6184,5506,5648,3907,6773]
weight = [9644,849,3232,3259,5229,314,5593,9600,6695,4340]
s=[(height[i],weight[i]) for i in range(len(height))]
s.sort(key=lambda x:(x[1],-x[0]))
ls=[s[i][0] for i in range(len(height))]
dp=[1]*len(height)
for i in range(1,len(height)):
    for j in range(i):
        if ls[i]>ls[j]:
            dp[i]=dp[j]+1
print(max(dp))



