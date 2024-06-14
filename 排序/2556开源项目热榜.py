N=eval(input())
weight=list(map(int,input().split()))
namex=[]
Statistics_Value=[]
heat=[]
for i in range(N):
    x=input().split()
    y=[x[0]]+list(map(int,x[1:]))
    namex.append(y[0])
    Statistics_Value.append(y[1:6])
    sumx=0
    for i in range(1,6):
        sumx+=weight[i-1]*y[i]
    heat.append(sumx)
# namex.sort(key=lambda x:(heat[-namex.index(x),x]))
ans=sorted(zip(namex,heat),key=lambda x:(-x[1],x[0]))
for i in ans:
    print(i[0])


