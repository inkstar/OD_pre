x=eval(input())
ans=[]
if (x<=4):
    print(x)
elif x%3==2:
    ans=[2]+[3]*(x//3)
elif x%3==0:
    ans=[3]*(x//3)
elif x%3==1:
    ans=[3]*(x//3-1)+[4]
print(*ans)