nums=[2,3,0,1,4]
FarReach=0
JumpTimes=0
CurrentPosition=0
for i in range(len(nums)):
    FarReach=max(FarReach,i+nums[i])
    if i==CurrentPosition:
        CurrentPosition=i+FarReach
        JumpTimes+=1
if FarReach>=len(nums)-1:
    print(JumpTimes)
