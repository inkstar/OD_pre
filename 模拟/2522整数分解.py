# 模拟
from math import sqrt
t=eval(input())
ans=[]
def split(x,a):
    tmp=[]
    n=x/a
    if (a%2==1 and x%a==0) or (a%2==0 and x/a-x//a==0.5):
        s1=n-(a-1)//2
        if s1>0:
            for j in range(a):
                tmp.append(int(s1+j))
            ans.append(tmp)
for i in range(1,t//2):
    split(t,i)
for i in range(len(ans)):
    print(f"{t}={'+'.join(map(str,ans[i]))}")

print(f"Result:{len(ans)}")

