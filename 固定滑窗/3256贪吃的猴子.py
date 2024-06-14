from math import inf
num=eval(input())
numbers=list(map(int,input().split()))
n=eval(input())
N=num-n
sumx=0
ans=inf
for i in range(num):
    sumx+=numbers[i]
    if i>=N-1:
        if i>N-1:
            sumx-=numbers[i-N]
        ans=min(ans,sumx)
print(sum(numbers)-ans)     
