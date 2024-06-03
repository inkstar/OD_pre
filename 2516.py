fixedn=eval(input())
n=eval(input())
s=[]
ans=[]
maxn=0
for _ in range(n):
    x=list(map(int,input().split(',')))
    maxn=max(maxn,len(x))
    s.append(x)
print(s)
# s = [[2, 5, 6, 7, 9, 5, 7], [1, 7, 4, 3, 4]]
t=n
times=1
while times<=maxn//fixedn+1:
    for i in s:
        for j in range(fixedn*times-fixedn,fixedn*times):
            if j<=len(i)-1:
                ans.append(i[j])
    times+=1
print(','.join(map(str,ans)))
