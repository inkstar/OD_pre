s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
black=[]
white=[]
go=[[0]*19 for _ in range(19)]
checklist=[[0]*19 for _ in range(19)]
for i in range(0,len(s1),2):
    black.append((s1[i],s1[i+1]))
    go[s1[i]][s1[i+1]]=1    #1为黑棋
for i in range(0,len(s2),2):
    white.append((s2[i],s2[i+1]))
    go[s2[i]][s2[i+1]]=2    #2为白旗

D=[(0,1),(0,-1),(1,0),(-1,0)]
ans=[0,0,0]
def dfs(x,y,key):
    global ans_black,ans_white
    for dx,dy in D:
        xn,yn=x+dx,y+dy
        if 0<=xn<19 and 0<=yn<19:
            if go[x][y]==key and go[xn][yn]==0 and checklist[xn][yn]==0:
                checklist[xn][yn]=1
                ans[key]+=1
for i in range(19):
    for j in range(19):
        dfs(i,j,1)
checklist=[[0]*19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        dfs(i,j,2)
print(f"{ans[1]} {ans[2]}")


