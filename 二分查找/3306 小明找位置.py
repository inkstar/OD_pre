lst=list(map(int,input().split(',')))
target=eval(input())
left=-1
right=len(lst)
while left+1<right:
    mid=(left+right)//2
    if lst[mid]>target:
        right=mid
    else:
        left=mid
print(right+1)