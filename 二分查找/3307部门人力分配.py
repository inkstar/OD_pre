M=eval(input())
requirements=list(map(int,input().split()))
requirements.sort()
sumx=sum(requirements)
def cal(limit:int):
    left=0
    day=0
    right=len(requirements)-1
    while left<=right:
        if requirements[left]+requirements[right]<=limit:
            left+=1
            right-=1
            day+=1
        else:
            right-=1
            day+=1
    return day<=M

left=requirements[-1]
right=requirements[-1]+requirements[-2]
while left<=right:
    mid=(left+right)//2
    if cal(mid):
        right=mid-1
    else:
        left=mid+1
print(left)

