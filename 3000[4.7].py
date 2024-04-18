s=input().split(',')
M=[int(i) for i in s]
M.sort()
R=int(input())
maxx=-1
for i,first in enumerate(M[:-2]):
    if sum(M[i:i+3])>R:
        break
    m1,m2=i+1,len(M)-1
    
    while(m1<m2):
        second=M[m1]
        third=M[m2]
        sumx=first+second+third
        if sumx<=R:
            maxx=max(maxx,sumx)
            m1+=1
        elif sumx>R:
            maxx=max(maxx,sumx)
            m2-=1

print(maxx)
