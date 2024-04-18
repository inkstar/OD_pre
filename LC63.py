obstacleGrid = [[0,1],[0,0]]
m=len(obstacleGrid)
n=len(obstacleGrid[0])
f=[[0]*n for i in range(m)]
f[0][0]=1
for i in range(0,m):
    for j in range(0,n):
        if obstacleGrid[i][j]==1:
            f[i][j]=0
print(f)
for j in range(1,n):
    if obstacleGrid[0][j]==1:
        break
    f[0][j]=f[0][j-1]
for i in range(1,m):
    if obstacleGrid[i][0]==1:
        break
    f[i][0]=f[i-1][0]
print(f)
for i in range(1,m):
    for j in range(1,n):
        if obstacleGrid[i][j]==1:
            continue
        else:
            f[i][j]=f[i][j-1]+f[i-1][j]
        # print(f[i][j])
print(f)
print(f[m-1][n-1])