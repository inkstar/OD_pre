N=eval(input())
lst=list(map(int,input().split()))
T=eval(input())
from collections import Counter
cnt=Counter(lst)
ans=[]
for i in cnt.keys():
    if cnt[i]>=T:
        ans.append((i,cnt[i]))
ans.sort(key=lambda x:(-x[1]))
print(len(ans))
for i in ans:
    print(i[0])