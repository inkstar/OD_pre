n=eval(input())
weight=list(map(int,input().split()))
def melt(z,y,x):
    s=[x,y,z]
    if x==y and y!=z:
        weight.append(z-y)
    elif x!=y and y==z:
        weight.append(y-x)
    elif x!=y and y!=z:
        t=abs((z-y)-(y-x))
        if t!=0:
            weight.append(abs((z-y)-(y-x)))

while len(weight)>2:
    weight.sort()
    melt(weight.pop(),weight.pop(),weight.pop())

weight.sort()
if len(weight)==2 or len(weight)==1:
    print(weight[-1])
else:
    print(0)
