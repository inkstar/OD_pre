s=input()
stack=[]
num=-1
lc=[0]*5
for i,x in enumerate(s):
    if x=='q' and i<=len(s)-5:
        lc[(i+1)%5]=1
print(sum(lc))

