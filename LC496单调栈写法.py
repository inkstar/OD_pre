nums1=[4,1,2]
nums2=[1,3,4,2]
stack=[]
ans={}
for i in nums2:
    while stack and stack[-1]<i:
        ans[stack.pop()]=i
    stack.append(i)
while stack:
    ans[stack.pop()]=-1
print([ans[i] for i in nums1])

