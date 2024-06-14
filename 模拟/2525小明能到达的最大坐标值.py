n=eval(input())
m=eval(input())
command=list(map(int,input().split()))
ans=0
tmpsum=0
for i in command:
    if i==m:
        if i<0:i-=1
        else:i+=1
    tmpsum+=i
    ans=max(ans,tmpsum)
print(ans)
