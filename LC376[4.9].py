nums=[1,17,5,10,13,15,10,5,16,8]
state=0 # 1表示上升 2表示下降
ans=0
if len(nums)<=2:
    print(len(nums))
for i in range(1,len(nums)):
    if state==0:
        ans=2
        if nums[i]>nums[i-1]:
            state=1
        elif nums[i]<nums[i-1]:
            state=2
        elif nums[i]==nums[i-1]:
            state=0
    elif state==1:
        if nums[i]<nums[i-1]:
            state=2
            ans+=1
    elif state==2:
        if nums[i]>nums[i-1]:
            state=1
            ans+=1
print(ans)
