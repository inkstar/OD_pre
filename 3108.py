number=eval(input())
days=eval(input())
item=list(map(int,input().split()))
item_price=[]
for _ in range(number):
    s=list(map(int,input().split()))
    item_price.append(s)
sumx=0
for i in range(number):
    for j in range(1,days):
        if item_price[i][j]>item_price[i][j-1]:
            sumx+=((item_price[i][j]-item_price[i][j-1])*item[i])
print(sumx)

