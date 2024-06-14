m,n,k=map(int,input().split())
grid=[]
D=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(m):
    s=list(map(int,input().split()))
    grid.append(s)
from collections import deque
q=deque()
top=0
step=0
ans=[0,0]

checklist=[[0]*n for _ in range(m)]
checklist[0][0]=1
q.append((0,0))

while(len(q)>0):
    step+=1
    for _ in range(len(q)):
        x,y=q.popleft()
        cur_height=grid[x][y]
        if cur_height>top:
            top=cur_height
            ans=[top,step]
        if cur_height==top and step<ans[1]:
            ans=[top,step]
        for dx,dy in D:
            xn,yn=x+dx,y+dy
            if 0<=xn<m and 0<=yn<n:
                if checklist[xn][yn]==0:
                    if -k<=cur_height-grid[xn][yn]<=k:
                        checklist[xn][yn]=1
                        q.append((xn,yn))
ans[1]-=1
if ans[1]!=0:
    print(*ans)
else:
    print('0 0')

                

