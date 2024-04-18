number=int(input())
days=int(input())
item=[]
item=input().split()
item=[int(i) for i in item]
price=[]
MaxProfit=0
for i in range(number):
    x=input().split()
    price.append([int(j) for j in x])
for i in range(number):
    for j in range(1,days-1):
        if price[i][j]-price[i][j-1]>0:
            MaxProfit+=price[i][j]-price[i][j-1]
print(MaxProfit)





print(item)
print(price)
    