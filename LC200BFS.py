grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
from collections import deque
m=len(grid)
n=len(grid[0])
s=deque()
checklist=[[0]*n for i in range(m)]
DIRECTIONS=[(-1,0),(1,0),(0,-1),(0,1)]
area=0
def bfs(x:int,y:int):
    global area
    area+=1
    checklist[x][y]=1
    while(s):
        x,y=s.popleft()
        for dx,dy in DIRECTIONS:
            next_x,next_y=x+dx,y+dy
            if (0<=next_x<m and 0<=next_y<n) and checklist[next_x][next_y]==0\
                and grid[next_x][next_y]=='1':
                s.append((next_x,next_y))
                bfs(next_x,next_y)
        
num=0

for i in range(m):
    for j in range(n):
        if grid[i][j]=='1' and checklist[i][j]==0:
            s.append((i,j))
            bfs(i,j)
            num+=1
print(area)
