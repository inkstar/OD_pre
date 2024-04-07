s=input()
from collections import Counter
mycount=Counter(s)
mystack=[]
used=set()
for i in s:
    if i in used:
        mycount[i]-=1
    else:
        while mystack and i>mystack[-1] and mycount[mystack[-1]]>1:
            used.remove(mystack[-1])
            mycount[mystack[-1]]-=1
            mystack.pop()
        mystack.append(i)
        used.add(i)
print(''.join(mystack))

