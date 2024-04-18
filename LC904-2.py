fruits=[0,1,2,2]
from collections import Counter
h=Counter()
maxx=0
left=0
for right in range(len(fruits)):
    h[fruits[right]]+=1
    while len(h)==3:
        left_num=fruits[left]
        h[left_num]-=1
        
        if h[left_num]==0:
            del h[left_num]
        left+=1    
    maxx=max(maxx,right-left+1)
print(maxx)
        
