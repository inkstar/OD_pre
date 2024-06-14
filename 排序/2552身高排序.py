H,N=map(int,input().split())
children=list(map(int,input().split()))
ls=[]
for i in children:
    ls.append([i,abs(i-H)])
ls.sort(key=lambda x:(x[1],x[0]))
for i in range(N):
    print(ls[i][0],end=' ')
              