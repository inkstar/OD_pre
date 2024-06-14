M=eval(input())
nums=list(map(int,input().split()))
nums_new=set(nums)
nums_new=list(nums_new)
M=len(nums_new)
N=eval(input())
ans=0
if N*2>M:
    print('-1')
else:
    nums_new.sort()
    ans+=sum(nums_new[0:N])
    ans+=sum(nums_new[(M-N):M])
    print(ans)

