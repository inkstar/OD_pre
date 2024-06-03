s=list(map(int,input().split()))
import math
n=len(s)
sums=sum(s)
minx=sums//8
num=0
i=minx
flag=0
ans=-1
# print(minx,ans)
if n>8:
    print(-1)
elif n==8:
    print(max(s))
else:
    while i<=max(s):
        for j in range(len(s)):
            num+=math.ceil(s[j]/i)
            # print(i,j,s[j],num)
            if num>8:
                i=i+1
                num=0
                break
            if j==len(s)-1 and num<=8:
                ans=i
                i=max(s)+1
    print(ans)
