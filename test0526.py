import bisect
import math
s=[-3,-2,-1,0,0,1,2]

neg = bisect.bisect_left(s, 0)
pos = bisect.bisect_right(s, 0)
print(neg,pos)
