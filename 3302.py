s=input().split()
SUM=int(s[0])
bucketBallNums=int(s[1])
bucket=input().split()
bucket=[int(k) for k in bucket]
left=int(SUM//bucketBallNums)
right=max(bucket)
mid=(left+right)//2
ls=[]
if sum(bucket)>SUM:
    def Maxx(maxCapacity,bucket):
        return sum(min(maxCapacity,k) for k in bucket)
    while left<right:
        if Maxx(mid,bucket)<=SUM:
            left=mid+1
            mid=(left+right)//2
        elif Maxx(mid,bucket)>SUM:
            right=mid
            mid=(left+right)//2
    if Maxx(mid,bucket)>SUM:
        ans=mid-1
    else:
        ans=mid
    for i in bucket:
        if i>ans:
            ls.append(i-ans)
        else:
            ls.append(0)
print(ls)