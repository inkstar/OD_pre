grid=[]
while(True):
    try:
        s=input().split()
        x=[]
        for i in s:
            if i=='YES':x.append(2)
            elif i=='NO':x.append(1)
            elif i=='NA':x.append(0)
        grid.append(x)
    except EOFError:
        break
#grid 录入没问题
from collections import deque
m=len(grid)
n=len(grid[0])
checklist=[[0]*n for _ in range(m)]
canable_num=0
q=deque()

for i in range(m):
    for j in range(n):
        if grid[i][j]==2:
            checklist[i][j]=1
            q.append((i,j))
        elif grid[i][j]==1:
            canable_num+=1
if canable_num==0:
    print(0)
day=0
D=[(0,1),(0,-1),(1,0),(-1,0)]
while len(q)>0:
    qsize=len(q)
    for _ in range(qsize):
        i,j=q.popleft()
        for dx,dy in D:
            next_x,next_y=i+dx,j+dy
            if 0<=next_x<m and 0<=next_y<n and checklist[next_x][next_y]==0 and\
                grid[next_x][next_y]==1:
                q.append((next_x,next_y))
                checklist[next_x][next_y]=1
                canable_num-=1
    if len(q)==0:
        break
    day+=1

if canable_num!=0:
    print(-1)
else:
    print(day)
