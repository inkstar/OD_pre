s=list(map(int,input().split()))
x,y=map(int,input().split())
m,n=s[0],s[1]
matrix=[[0 for _ in range(n)] for _ in range(m) ]
x1,x2=0,0
curr=0
for i in range(2,len(s),2):
    curr=s[i+1]
    while(curr>0):
        if x2<=n-1:
            matrix[x1][x2]+=s[i]
            x2+=1
            curr-=1
        else:
            x1+=1
            x2=0
print(matrix[x][y])
    

# print(s)