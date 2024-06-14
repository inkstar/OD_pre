n,m=map(int,input().split())
target=input()
grid=[]
for i in range(n):
    s=input()
    grid.append(s)
checklist=[[0]*m for _ in range(n)]
D=[(0,1),(0,-1),(1,0),(-1,0)]
flag=0
ansflag=0
           
def dfs(x:int,y:int):
    global ansflag,flag
    
    checklist[x][y]=1
    for dx,dy in D:
        xn,yn=x+dx,y+dy
        if 0<=xn<n and 0<=yn<n and checklist[xn][yn]==0 and grid[xn][yn]==target[flag]:
            if flag==len(target)-1:
                ansflag=1
                return
            checklist[xn][yn]=1
            flag+=1
            dfs(xn,yn)
            checklist[xn][yn]=0
    flag-=1
for i in range(m):
    for j in range(n):
        if checklist[i][j]==0 and grid[i][j]==target[0]:
            flag+=1
            checklist[i][j]=1
            dfs(i,j)
            checklist[i][j]=0
            if ansflag==1:
                print(i+1,j+1)
                break
    if ansflag==1:break
if ansflag==0:
    print('NO')


'''
5 5
HELLOWORLD
CPUCY
EKLQH
CHELL
LROWO
DGRBC
'''