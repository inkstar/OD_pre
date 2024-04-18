A=input()
s=list(input())
maxx=0
from collections import Counter
h=Counter()
left=0
for right,ch in enumerate(s):
    h[ch]+=1
    if ch==A:
        while len(h)>0:
            del h[s[left]]
            left+=1
            print(ch,h)
    else:
        while h[ch]>2:
            h[s[left]]-=1
            left+=1
    maxx=max(maxx,right-left+1)
print(maxx)
    