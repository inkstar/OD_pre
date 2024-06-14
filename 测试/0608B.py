m,n,k=map(int,input().split())
grid=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if i//10+i%10+j//10+j%10<=k:
            grid[i][j]=1
from collections import deque
q=deque()
checklist=[[0]*n for _ in range(m)]
checklist[0][0]=1
q.append((0,0))
D=[(0,1),(0,-1),(1,0),(-1,0)]
ans=0
while len(q)>0:
    for _ in range(len(q)):
        x,y=q.popleft()
        for dx,dy in D:
            xn,yn=x+dx,y+dy
            if 0<=xn<m and 0<=yn<n:
                if grid[xn][yn]==1 and checklist[xn][yn]==0:
                    ans+=1
                    q.append((xn,yn))
                    checklist[xn][yn]=1
print(ans+1)
