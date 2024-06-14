n,m=map(int,input().split())
col= n//m if n%m==0 else n//m+1
matrix=[[0]*col for _ in range(m)]
sumx=m*col
num=1

top,bottom=0,m-1
left,right=0,col-1
while top<=bottom and left<=right:
    #遍历上边界
    for i in range(left,right+1):
        matrix[top][i]=num if num<=n else '*'
        num+=1
    top+=1
    #遍历右边界
    for i in range(top,bottom+1):
        matrix[i][right]=num if num<=n else '*'
        num+=1
    right-=1
    #遍历下边界
    if top<=bottom:
        for i in range(right,left-1,-1):
            matrix[bottom][i]=num if num<=n else '*'
            num+=1
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            matrix[i][left]=num if num<=n else '*'
            num+=1
        left+=1
for i in range(m):
    print(*matrix[i])




    