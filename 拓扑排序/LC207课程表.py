numCourses = 2
prerequisites = [[1,0]]
from collections import defaultdict
from collections import deque
h=defaultdict(list)
inDegreelist=[0]*numCourses
for a,b in prerequisites:
    h[a].append(b)
    inDegreelist[a]+=1

q=deque()
for i in range(numCourses):
    if inDegreelist[i]==0:
        q.append(i)

while len(q)>0:
    cur=q.popleft()
    for nxt in h[cur]:
        inDegreelist[nxt]-=1
        if inDegreelist[nxt]==0:
            q.append(nxt)

return not all(inDegreelist)

