grid = [[2,1,1],[1,1,0],[0,1,1]]
from collections import deque
n=len(grid)
m=len(grid[0])

checklist=[[0]*m for _ in range(n)]
level=0
fresh_num=0
q=deque()
DIRECTIONS=[(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    for j in range(m):
        if grid[i][j]==2:
            checklist[i][j]=1
            q.append((i,j))
        elif grid[i][j]==1:
            fresh_num+=1
if fresh_num==0:
    print(0)
    # return 0
while len(q)>0:
    qsize=len(q)
    level+=1
    for _ in range(qsize):
        i,j=q.popleft()
        for dx,dy in DIRECTIONS:
            next_i,next_j=i+dx,j+dy
            if 0<=next_i<n and 0<=next_j<m and checklist[next_i][next_j]==0 and\
                grid[next_i][next_j]==1:
                checklist[next_i][next_j]=1
                fresh_num-=1
                q.append((next_i,next_j))
# print(fresh_num)
if fresh_num!=0:
    print(-1)
else:
    print(level-1)

