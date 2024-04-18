M=eval(input())
L=list(map(int,input().split()))

left=0
maxx=0
sum=0

for right,x in enumerate(L):
    sum+=x
    if sum<=M:
        maxx=max(maxx,sum)
    else:
        while(sum>M):
            sum-=L[left]
            left+=1
        maxx=max(maxx,sum)
print(maxx)
        
    


