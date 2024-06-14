#还没解决

M,N=map(int,input().split())
x0,y0=0,0
grid=[]
for i in range(M):
    s=list(input())
    grid.append(s)
print(grid)
flag=0
for i in range(M):
    for j in range(N):
        if grid[i][j]=='S':
            flag+=1
            x0,y0=i,j
        if grid[i][j]=='E':
            flag+=1
            xe,ye=i,j
    if flag==2:break

from collections import deque
from math import inf
q=deque()
step=0
D=[(0,1),(0,-1),(1,0),(-1,0)]
checklist=[[inf]*N for _ in range(M)]
checklist[x0][y0]=0
for d,(dx,dy) in enumerate(D):
    xn,yn=x0+dx,y0+dy
    if 0<=xn<M and 0<=yn<N and grid[xn][yn]!='X':
        q.append([xn,yn,1,d])
        checklist[xn][yn]=1
ans=M*N+1

while len(q)>0:
    for _ in range(len(q)):
        x,y,cur_step,cur_dir=q.popleft()
        for nx_dir,(dx,dy) in enumerate(D):
            xn,yn=x+dx,y+dy
            if 0<=xn<M and 0<=yn<N:
                if grid[xn][yn]!='X':
                    if nx_dir==cur_dir:
                        nxt_step=cur_step+1
                    else:
                        nxt_step=cur_step+2
                    if nxt_step<=checklist[xn][yn]:
                        checklist[xn][yn]=nxt_step
                        q.append((xn,yn,nxt_step,nx_dir))
ans=checklist[xe][ye]                 
if ans==inf:
    print(-1)
else:
    print(ans)





