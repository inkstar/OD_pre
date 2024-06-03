n=eval(input())
f=[0]*51
f[0]=1
f[1]=1
f[2]=1
f[3]=2
for i in range(4,n+1):
    f[i]=f[i-1]+f[i-3]
print(f[n])