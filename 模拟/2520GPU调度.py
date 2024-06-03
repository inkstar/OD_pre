import math
N=eval(input())
lenx=eval(input())
task=list(map(int,input().split()))
print(N,lenx,task)
ans=0
sumtask=0
for i in range(lenx):
    sumtask+=task[i]
    print(i,sumtask,ans)
    if sumtask<=N:
        sumtask=0
        ans+=1
    else:
        sumtask-=N
        ans+=1
    print(i,sumtask,ans)
if sumtask%N==0:
    ans+=sumtask//N
else:
    ans+=sumtask//N+1
print(ans)