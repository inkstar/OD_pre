m,n=map(int,input().split())
grid=[]
for _ in range(m):
    s=list(map(int,input().split()))
    grid.append(s)
direction=[(-1,0),(1,0),(0,1),(0,-1),(0,0)]
sumx=0
for i in range(m):
    for j in range(n):
        flag=0
        for di,dj in direction:
            x,y=i+di,j+dj
            if (0<=x<m and 0<=y<n) and grid[x][y]==1:
                flag=1
        sumx+=flag
print(sumx)