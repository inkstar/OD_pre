N=eval(input())
height=list(map(int,input().split()))
ans=[0]*len(height)
for i,x in enumerate(height):
    for j in range(i+1,len(height)):
        if height[j]>height[i]:
            ans[i]=j
            break
print(*ans)
