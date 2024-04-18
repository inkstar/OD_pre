color=list(map(int,input().split()))
time=int(input())
maxx=0
from collections import Counter
h=Counter(color[0:time])
left=0
maxx=max(h.values())
sumx=0
# print(maxx,h)
for right in range(time,len(color)):
    h[color[right]]+=1
    left_num=color[left]
    h[left_num]-=1
    left+=1
    sumx=max(h.values())
    maxx=max(maxx,sumx)
print(maxx)

