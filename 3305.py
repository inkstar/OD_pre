from math import inf
from math import ceil
peace=list(map(int,input().split()))
N=len(peace)
H=eval(input())
MinSpeed=inf
left=1
right=max(peace)
def Eatpeace(speed:int,s:list):
    totaltime=0
    for i in s:
        totaltime+=ceil(i/speed)
    # print(speed,totaltime)
    return (totaltime<=H)
# print(left,right)
# print(peace)
while left<=right:
    mid=(left+right)//2
    if Eatpeace(mid,peace)==1:
        right=mid-1
    elif Eatpeace(mid,peace)==0:
        left=mid+1
    # print(left,right,mid,Eatpeace(mid,peace))
if left==max(peace) and left*H<=sum(peace):
    print(0)
else:
    print(left)
