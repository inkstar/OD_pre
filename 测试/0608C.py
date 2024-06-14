n=eval(input())
level=list(map(int,input().split()))
from collections import defaultdict
ls=defaultdict(int)
lb=defaultdict(int)
rs=defaultdict(int)
rb=defaultdict(int)
ans=0
for i in range(1,len(level)-1):
    for j in range(0,i):
        if level[j]<level[i]:
            ls[i]+=1
        elif level[j]>level[i]:
            lb[i]+=1
for i in range(1,len(level)-1):
    for j in range(i+1,len(level)):
        if level[j]<level[i]:
            rs[i]+=1
        elif level[j]>level[i]:
            rb[i]+=1
for i in range(1,len(level)-1):
    ans+=ls[i]*rb[i]
    ans+=lb[i]*rs[i]
print(ans)

