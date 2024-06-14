n=eval(input())
ans=0
level=list(map(int,input().split()))
left_small=[0]*n
left_big=[0]*n
right_small=[0]*n
right_big=[0]*n
for i in range(1,n):
    for j in range(i):
        if level[j]<level[i]:left_small[i]+=1
        elif level[j]>level[i]:left_big[i]+=1
for i in range(n-1):
    for j in range(i+1,n):
        if level[j]<level[i]:right_small[i]+=1
        elif level[j]>level[i]:right_big[i]+=1
for i in range(1,n-1):
    ans+=(left_small[i]*right_big[i]+left_big[i]*right_small[i])
print(ans)