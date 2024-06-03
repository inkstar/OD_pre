grid = [[1,0,1],[1,0,0],[1,0,0]]
D=[(-1,0),(1,0),(0,-1),(0,1)]
m=len(grid)
n=len(grid[0])
num=0
for i in range(m):
    for j in range(n):
        if grid[i][j]==1:
            
            sum=0
            t=0
            ls=[0,0,0,0]
            for di,dj in D:
                x=i+di
                y=j+dj
                if 0<=x<=m-1 and 0<=y<=n-1 and grid[x][y]==1:
                    sum+=1
                    ls[t]=1
                t+=1
            if sum==4:
                num+=4
            elif sum==3:
                num+=2
            elif sum==2:
                if ls[0]+ls[1]==2 or ls[2]+ls[3]==2:
                    continue
                else:
                    num+=1
            print(i,j,sum)
print(num)       
            