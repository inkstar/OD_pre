N,M=map(int,input().split())
grid=[]
for _ in range(N):
    s=list(map(int,input().split()))
    grid.append(s)
# print(grid) 
DIRECTIONS=[(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
checklist=[[0]*M for _ in range(N)]
ans=0
def DFS(x:int,y:int):
    checklist[x][y]=1
    for dx,dy in DIRECTIONS:
        next_x,next_y=x+dx,y+dy
        if (0<=next_x<N and 0<=next_y<M) and checklist[next_x][next_y]==0 and\
            grid[next_x][next_y]==1:
            DFS(next_x,next_y)

for i in range(N):
    for j in range(M):
        if grid[i][j]==1 and checklist[i][j]==0:
            DFS(i,j)
            ans+=1
print(ans)

