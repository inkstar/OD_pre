s=list(input().split())
print(s)
from collections import deque,defaultdict
h=defaultdict(list)     #邻接表
inDegree=defaultdict(int)
for x in s:
    h[x[-1]].append(x[0])
    inDegree[x[0]]+=1
ans=[]
# print(inDegree)
for i in h.keys():
    if inDegree[i]==0:
        ans.append(i)
ans.sort()
q=deque(ans)
while len(q)>0:
    new_ls=[]
    for _ in range(len(q)):
        cnt=q.popleft()
        h[cnt].sort()
        for nxt in h[cnt]:
            inDegree[nxt]-=1
            if inDegree[nxt]==0:
                new_ls.append(nxt)
                q.append(nxt)
    new_ls.sort()
    ans+=new_ls
print(*ans)

