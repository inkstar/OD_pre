wa,wb,wt,pa,pb=map(int,input().split())
numa=wt//wa+1
numb=wt//wb+1
ans=0
f=[[0]*numa for _ in range(numb)]
weight=[[0]*numa for _ in range(numb)]
for i in range(1,numb):
    for j in range(1,numa):
        weight[i][j]+=i*wb+j*wa
        f[i][j]+=i*pb+j*pa
        if weight[i][j]==wt:
            ans=max(ans,f[i][j])
print(ans)

    