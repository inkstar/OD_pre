nums1=input().split()
m = int(input())
nums2=input().split()
n = int(input())
t=m+n-1
m=m-1
n=n-1
while(nums2):
    if(nums2[n]>nums1[m]):
        nums1[t]=nums2[n]
        nums2.pop()
        n=n-1
        t=t-1
    else:
        nums1[t]=nums1[m]
        m=m-1
        t=t-1
print(nums1)
