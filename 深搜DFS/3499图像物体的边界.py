M,N=map(int,input().split())
grid=[]
for i in range(M):
    s=list(map(int,input().split()))
    grid.append(s)
D=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(M):
    for j in range(N):
        if grid[i][j]==5:
            for dx,dy in D:
                xn,yn=i+dx,j+dy
                if 0<=xn<M and 0<=yn<N:
                    if grid[xn][yn]==1:
                        grid[xn][yn]=3
checklist=[[0]*N for _ in range(M)]
ans=0
def dfs(x,y):
    checklist[x][y]=1
    for dx,dy in D:
        xn,yn=x+dx,y+dy
        if 0<=xn<M and 0<=yn<N:
            if grid[xn][yn]==3 and checklist[xn][yn]==0:
                dfs(xn,yn)
                checklist[xn][yn]=1
for i in range(M):
    for j in range(N):
        if grid[i][j]==3 and checklist[i][j]==0:
            dfs(i,j)
            ans+=1
print(ans)
print(grid)