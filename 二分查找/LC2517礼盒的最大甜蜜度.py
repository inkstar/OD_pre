price=[1,3,1]
k=2
price.sort()
left=0
right=price[-1]-price[0]
def check(x:int):
    i=0
    j=0
    cnt=1
    while j<len(price):
        if price[j]-price[i]>=x:
            cnt+=1
            i=j
        j+=1
    return cnt

while left<right:
    mid=(left+right+1)//2
    if check(mid)>=k:
        left=mid
    else:
        right=mid-1
print(left)