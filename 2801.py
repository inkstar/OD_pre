s=input()
from collections import Counter
s2=Counter(s)

Min=min(s2.values())
s3=[]
for i,j in s2.items():
    if j!=Min:
        s3.append(i)
sm=[i for i in s if i in s3]
if len(sm)>0:
    print(''.join(sm))
else:
    print("empty")



