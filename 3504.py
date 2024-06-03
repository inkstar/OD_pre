# matrix=[]
# while(True):
#     try:
#         s=list(map(int,input().split()))
#         matrix.append(s)
#     except:
#         break
matrix=[[1,0,0],[0,1,0],[0,0,1]]
DIRECTIONS=[(0,-1),(0,1),(-1,0),(1,0)]
N=len(matrix)
checklist=[0]*N

def dfs(x:int):
    checklist[x]=1
    for i in range(N):
        if checklist[i]==0 and matrix[x][i]==1:
            dfs(i)
            print(i)
ans=0
for i in range(N):
    if checklist[i]==0:
        dfs(i)
        ans+=1
        # print(ans)
print(ans)
# print(matrix[0][0])
# print(checklist)
