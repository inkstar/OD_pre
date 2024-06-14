price=list(map(int,input().split()))
n=len(price)
stack=[]

ans=price.copy()
# print(price)
for i in range(2*n):
    while stack and price[i%n]<price[stack[-1]]:
        tmp=stack.pop()
        ans[tmp]+=price[i%n]+price[tmp]
    stack.append(i%n)
print(*ans)

