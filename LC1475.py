prices=[8,4,6,2,3]
stack=[]
for i,num in enumerate(prices):
    flag=0
    for j in range(i+1,len(prices)):
        if flag==0 and prices[j]<prices[i]:
            stack.append(prices[i]-prices[j])
            flag=1
        else:
            continue
    if flag==0:
        stack.append(prices[i])
print(stack)