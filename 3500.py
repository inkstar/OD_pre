DIRECTIONS=[(-1,0),(1,0),(0,-1),(0,1)]
M,N=map(int,input().split())
grid=[]
for _ in range(M):
    s=list(map(int,input().split()))
    grid.append(s)
checklist=[[0]*N for _ in range(M)]
maxx=0
def dfs(x:int,y:int):
    global num
    num+=1
    checklist[x][y]=1
    for dx,dy in DIRECTIONS:
        next_x,next_y=x+dx,y+dy
        if (0<=next_x<M and 0<=next_y<N) and checklist[next_x][next_y]==0 and\
            -1<=grid[next_x][next_y]-grid[x][y]<=1:
            dfs(next_x,next_y)

for i in range(M):
    for j in range(N):
        if checklist[i][j]==0:
            num=0
            dfs(i,j)
            maxx=max(maxx,num)
            

print(maxx)