n=eval(input())
grid=[]
for _ in range(n):
    s=list(map(int,input().split()))
    grid.append(s)
checklist=[0]*n
maxx=0
# global ans
def dfs(x:int):
    global ans      
    checklist[x]=1
    ans+=1
    for k in range(n):
        if k!=x and checklist[k]==0 and grid[k][x]==1:
            dfs(k)
for i in range(n):
    if checklist[i]==0:
        ans=0
        dfs(i)
        maxx=max(maxx,ans)
print(maxx)