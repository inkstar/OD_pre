grid=[]
while True:
    try:
        s=input()
        if len(s)==0:
            break
        grid.append(s)
    except:
        break
m=len(grid)
n=len(grid[0])
DIRECTIONS=[(-1,0),(1,0),(0,1),(0,-1)]

checklist=[[0]*n for _ in  range(m)]

def DFS(x:int,y:int):
    global myvalue
    checklist[x][y]=1
    myvalue+=int(grid[x][y])
    for dx,dy in DIRECTIONS:
        next_x,next_y=x+dx,y+dy
        if (0<=next_x<m and 0<=next_y<n) and grid[next_x][next_y]!='0'\
            and checklist[next_x][next_y]==0:
            DFS(next_x,next_y)


maxx=0
for i in range(m):
    for j in range(n):
        if grid[i][j]!='0' and checklist[i][j]==0:
            myvalue=0
            DFS(i,j)
            maxx=max(maxx,myvalue)
print(maxx)