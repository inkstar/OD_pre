from collections import defaultdict
n=eval(input())
f=defaultdict(int)
f[1]=2
f[2]=1
f[3]=1
f[4]=2
f[5]=2
f[6]=2
if n<=6:
    print(f[n])
else:
    for i in range(7,n):
        f[i]=min(f[2]+f[i-2],f[3]+f[i-3])
    print(f[n])
