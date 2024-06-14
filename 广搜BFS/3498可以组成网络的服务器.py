n,m=map(int,input().split())
grid=[]
ans=0
tmpans=0
for i in range(n):
    x=list(map(int,input().split()))
    grid.append(x)
D=[(0,1),(0,-1),(1,0),(-1,0)]
checklist=[[0]*m for _ in range(n)]

from collections import deque
for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and checklist[i][j]==0:
            checklist[i][j]=1
            q=deque()
            q.append((i,j))
            tmpans=0
            while len(q)>0:
                x,y=q.popleft() 
                tmpans+=1
                checklist[x][y]=1
                for dx,dy in D:
                    xn,yn=x+dx,y+dy
                    if 0<=xn<n and 0<=yn<m:
                        if checklist[xn][yn]==0 and grid[xn][yn]==1:
                            q.append((xn,yn))
                            # checklist[xn][yn]=1
            ans=max(ans,tmpans)
print(ans)







# def dfs(x:int,y:int):
#     global tmpans
#     checklist[x][y]=1
#     tmpans+=1
#     for dx,dy in D:
#         xn,yn=x+dx,y+dy
#         if 0<=xn<n and 0<=yn<m:
#             if checklist[xn][yn]==0 and grid[xn][yn]==1:
#                 dfs(xn,yn)

# for i in range(n):
#     for j in range(m):
#         if checklist[i][j]==0 and grid[i][j]==1:
#             dfs(i,j)
#             ans=max(ans,tmpans)
#             tmpans=0
# print(ans)


