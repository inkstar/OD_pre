taskNum=eval(input())
relationsNum=eval(input())
from collections import defaultdict
from collections import deque
h=defaultdict(list) #邻接表
inDegreelist=[0]*taskNum
q=deque()
for i in range(relationsNum):       #初始化记录关系，入度
    a,b=map(int,input().split())
    h[a].append(b)
    inDegreelist[b]+=1

for i in range(taskNum):            #初始化队列
    if inDegreelist[i]==0:
        q.append(i)
ans=0
while len(q)>0:
    s=[]
    cur=q.popleft()
    # while len(q)>0:
    #     cur=q.popleft()
    #     s.append(cur)
    # ans+=1
    # for cur in s:
    for nxt in h[cur]:
        inDegreelist[nxt]-=1
        if inDegreelist[nxt]==0:
            q.append(nxt)
print(ans)


