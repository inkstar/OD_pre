M,N,K=map(int,input().split())
L=int(input())
f=[0]*33
f_life=[M]*33
if M>K: #不考虑陷阱
    f[0]=1
    f[1]=2
    f[2]=4
    if N>2:
        for i in range(3,N+1):
            f[i]=f[i-1]+f[i-2]+f[i-3]
    print(f[N])
else: #考虑陷阱
    f[0]=1
    





