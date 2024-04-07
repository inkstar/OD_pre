temperatures=[73,74,75,71,69,72,76,73]
stack=[]
answer=[0]*len(temperatures)
for i,num in enumerate(temperatures):
    
    while len(stack)>0 and num>stack[-1][1]:
        answer[stack[-1][0]]=(i-stack[-1][0])
        stack.pop()
    stack.append([i,num])
    #print(i,stack,answer)
return answer