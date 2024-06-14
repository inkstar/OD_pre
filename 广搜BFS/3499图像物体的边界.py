M,N=map(int,input().split())
grid=[]
for i in range(M):
    s=list(map(int,input().split()))
    grid.append(s)
ans_lst=[]
for i in range(M):
    for j in range(N):
        if grid[i][j]==5:
            ans_lst.append((i,j))
def test_distance(a,b,x,y):
    if abs(a-x)<=3 and abs(b-y)<=3:return 1
    else:return 0
ans=len(ans_lst)
ans1=0
for x,y in ans_lst:
    for a,b in ans_lst:
        if (x,y)!=(a,b):
            ans1+=test_distance(x,y,a,b)
print(ans-ans1//2)
print(ans_lst)