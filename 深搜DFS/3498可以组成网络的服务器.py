n,m=map(int,input().split())
grid=[]
ans=0
tmpans=0
for i in range(n):
    x=list(map(int,input().split()))
    grid.append(x)
D=[(0,1),(0,-1),(1,0),(-1,0)]
checklist=[[0]*m for _ in range(n)]
def dfs(x:int,y:int):
    global tmpans
    checklist[x][y]=1
    tmpans+=1
    for dx,dy in D:
        xn,yn=x+dx,y+dy
        if 0<=xn<n and 0<=yn<m:
            if checklist[xn][yn]==0 and grid[xn][yn]==1:
                dfs(xn,yn)

for i in range(n):
    for j in range(m):
        if checklist[i][j]==0 and grid[i][j]==1:
            dfs(i,j)
            ans=max(ans,tmpans)
            tmpans=0
print(ans)


