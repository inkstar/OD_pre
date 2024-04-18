s=input()
average=len(s)/4
from collections import Counter
from math import inf
h=Counter(s)
hcnt=Counter()
left=0
minx=inf

hneed={k:v-average for k,v in h.items() if v>average}
def check(hcnt,hneed):
    return all(hcnt[k]>=hneed[k] for k in hneed)
for right,x in enumerate(s):
    hcnt[x]+=1
    while (check(hcnt,hneed)==True):
        minx=min(minx,right-left+1)
        hcnt[s[left]]-=1
        left+=1
print(minx)



