content=input()
word=input()
from collections import Counter
hw=Counter(word)
ht=Counter(content[0:len(word)])
sumx=0
left=0
if ht==hw:
    sumx+=1
for right in range(len(word),len(content)):
    ht[content[right]]+=1
    ht[content[left]]-=1
    left+=1
    if ht==hw:
        sumx+=1
print(sumx)