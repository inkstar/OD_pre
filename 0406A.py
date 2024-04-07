n=int(input())
s=[]
sum=0
for i in range(n):
    x=input()
    s.append(x)
L,keyword=input().split()
L=int(L)
for i in s:
    x=i.split('/')
    print(x)
    if(len(x)>=L+1 and keyword in x[L]):
        sum+=1


print(L,keyword)
print(type(L))
print(sum)

