M=eval(input())
N=eval(input())
A=[]
B=[]
sum=0
from collections import Counter
s1=input().split(' ')
A=list(s1)
s2=input().split(' ')
B=list(s2)
C=Counter(B)
for i in A:
    if i in B:
        sum+=C[i]
print(sum)


