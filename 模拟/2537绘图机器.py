N,E=map(int,input().split())
order=[]
measure=0
xy=[]
xy.append((0,0))
lastx=0
lasty=0
for i in range(N):
    x,y=map(int,input().split())
    order.append((x,y))
    measure+=abs(lasty)*(x-lastx)
    lastx=x
    lasty+=y
    xy.append((lastx,lasty))
measure+=abs(lasty)*(E-lastx)
print(measure)
# print(E)
# print(xy)
