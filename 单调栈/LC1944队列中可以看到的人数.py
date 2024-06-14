heights = [10,6,8,5,11,9]
stack=[]
ans=[0]*len(heights)
for i,x in enumerate(heights):
    while stack and x>stack[-1][1]:
        #ans[stack[-1][0]]=i-stack[-1][0]
        stack.pop()
    stack.append([i,x])

while stack:
    ans[stack[-1][0]]=len(heights)-1-stack[-1][0]
    stack.pop()
print(ans)