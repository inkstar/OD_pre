temperatures=[3,1,2,5,3]
stack=[]
ans=[0]*len(temperatures)
for i in range(len(temperatures)):
    while stack and temperatures[i]>stack[-1][1]:
        ans[stack[-1][0]]=i-stack[-1][0]
        stack.pop()
    stack.append([i,temperatures[i]])
print(ans)