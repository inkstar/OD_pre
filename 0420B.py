N=int(input())
wealth=list(map(int,input().split()))
dictx=[[] for i in range(N+1)]
maxx=0
sumx=0
for i in range(N-1):
    x,y=map(int,input().split())
    print(x,y)
    dictx[x].append(y)
    print(dictx)
# print(N,wealth,dictx)
for i in range(1,N+1):
    sumx+=wealth[i-1]
    if len(dictx[i])==1:
        sumx+=wealth[dictx[i][0]-1]
    elif len(dictx[i])>1:
        for j in range(len(dictx[i])):
            sumx+=wealth[dictx[i][j]-1]
    maxx=max(maxx,sumx)
    sumx=0
print(maxx)
