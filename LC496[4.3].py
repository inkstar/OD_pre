nums1=[4,1,2]
nums2=[1,3,4,2]
ans=[]
flag=0
for i in nums1:
    j=nums2.index(i)#j为i在nums2的坐标
    for x in range(j,len(nums2)):
        if flag==0 and nums2[x]>i:
            ans.append(nums2[x])
            flag=1
            x=len(nums2)-1
    if flag==0:
        ans.append(-1)
    flag=0
print()
