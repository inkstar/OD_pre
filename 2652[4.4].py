num1=list(input())
n=int(input())
stack=[]
restn=0
for no,i in enumerate(num1):
        while(stack and i<stack[-1] and restn<n):
            stack.pop()
            restn+=1
        stack.append(i)
print(''.join(stack[len(num1)-n]))
        
        