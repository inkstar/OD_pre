n=eval(input())
prices=[]
for i in range(n):
    price=eval(input())
    prices.append(price)
v=eval(input())
num=0
left=0
sumx=0
ans0=0  #存储临时总数
ansnum=0
for right in range(len(prices)):
    sumx+=prices[right]
    num+=1
    while sumx>v:
        sumx-=prices[left]
        left+=1
        num-=1
    if sumx<=v and num>ansnum:
        ansnum=num
print(ansnum)
        

    



