height = [4,2,0,3,2,5]
from collections import deque
stack=[]
ans=0

for num,i in enumerate(height):
    if len(stack)==0:
        stack.append(num)
    elif i<=height[stack[-1]]:
        stack.append(num)
    else:
        while stack and i>height[stack[-1]]:
            if len(stack)<=1:
                stack.pop()
                stack.append(num)
            else:
                mid=stack.pop()
                leftx=stack[-1]
                rightx=num
                h=(min(height[leftx],height[rightx])-height[mid])*(rightx-leftx-1)
                ans+=h
        stack.append(num)
print(ans)
