N=eval(input())
ill=list(map(int,input().split(',')))
ill_num0=len(ill)
grid=[]
for i in range(N):
    x=list(map(int,input().split(',')))
    grid.append(x)
checklist=[0]*N
from collections import deque
q=deque()
for i in ill:
    q.append(i)

while len(q)>0:
    qsize=len(q)
    for i in range(qsize):
        cnt=q.popleft()
        checklist[cnt]=1
        for j in range(N):
            if j!=cnt and grid[cnt][j]==1 and checklist[j]==0:
                q.append(j)
                ill.append(j)
print(len(set(ill))-ill_num0)
