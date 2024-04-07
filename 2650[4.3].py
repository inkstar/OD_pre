N=eval(input())
height=[int(x) for x in input().split()]
ans=[0]*N
stack=[]
for i,num in enumerate(height):
    while(stack and height[stack[-1]]<num):
        ans[stack.pop()]=i
    stack.append(i)


# print(N)
# print(height)
for i in ans:
    print(i,end=' ')