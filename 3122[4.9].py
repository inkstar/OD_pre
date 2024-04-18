s=input().split(',')
weight=[int(i) for i in s]
BiggestWeight=eval(input())
weight.sort()
sum=0
num=0
for i in weight:
    sum+=i
    if(sum>BiggestWeight):
        break
    num+=1
print(num)