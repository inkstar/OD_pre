nums=[1,1,1,2,2,3]
n=1
flag=0
for i in range(len(nums)):
    if nums[i]==nums[n-1]:
        if(flag==0):
            flag=flag+1
        elif flag==1:
            flag+=1
            n=n+1
            nums[n-1]=nums[i]
        elif flag==2:
            continue
    elif nums[i]!=nums[n-1]:
        flag=1
        n=n+1
        nums[n-1]=nums[i]
print(n,nums)