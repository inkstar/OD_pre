m,n=3,3
f=[[1]*n for i in range(m)]
# print(m,n,f)
for i in range(1,m):
    for j in range(1,n):
        f[i][j]=f[i][j-1]+f[i-1][j]
        # print(f[i][j])
print(f[m-1][n-1])