s=(input().split())
L=list(map(int,input().split()))
M=int(s[0])
N=int(s[1])
K=int(s[2])
f=[0]*N
# print(M,N,K,L)
f[0]=1
f[1]=1
f[2]=2

for i in range(3,N+1):
    f[i]=f[i-1]+f[i-2]+f[i-3]