nums=[2,3,1,1,4]
FarReach=0
CurrentPosition=0
MaxFar=0
for i in nums:
    MaxFar=max(MaxFar,i+nums[i])
    if i==CurrentPosition:
        CurrentPosition=MaxFar
        print(CurrentPosition)
# if CurrentPosition>=len(nums)-1:
#     return True
# return False