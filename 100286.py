# 129 双周赛
grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
flag=False
for i in range(3):
    for j in range(3):
        if grid[i][j]=='B':
            grid[i][j]=1
        else:
            grid[i][j]=0
a=[0,0,0,0]
a[0]=grid[0][0]+grid[0][1]+grid[1][0]+grid[1][1]
a[1]=grid[0][1]+grid[0][2]+grid[1][1]+grid[1][2]
a[2]=grid[1][0]+grid[1][1]+grid[2][0]+grid[2][1]
a[3]=grid[1][1]+grid[1][2]+grid[2][1]+grid[2][2]
if 1 in a or 3 in a:
    return True
else:
    return False