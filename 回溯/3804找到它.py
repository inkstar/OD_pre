n,m=map(int,input().split())
target=input()
grid=[]
for i in range(n):
    s=list(input())
    grid.append(s)
D=[(0,1),(0,-1),(1,0),(-1,0)]
checklist=[[0]*m for _ in range(n)]
flag=0

ansflag=0
def dfs(x:int,y:int):
    global ansflag,flag
    # checklist[x][y]=1
    for dx,dy in D:
        xn,yn=x+dx,y+dy
        if 0<=xn<n and 0<=yn<m and checklist[xn][yn]==0 and flag<len(target) and grid[xn][yn]==target[flag]:
            if flag==len(target)-1:
                ansflag=1
                return
            flag+=1
            checklist[xn][yn]=1
            dfs(xn,yn)
            checklist[xn][yn]=0  
    flag-=1
for i in range(n):
    for j in range(m):
        if checklist[i][j]==0 and flag<len(target) and grid[i][j]==target[flag]:
            flag+=1
            checklist[i][j]=1
            dfs(i,j)
            checklist[i][j]=0
            if ansflag==1:
                print(i+1,j+1)
                break
            flag=0
    if ansflag==1:break
if ansflag==0:print('NO')