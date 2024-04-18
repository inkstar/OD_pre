N=eval(input())
s=[]
for i in range(N):
    TL=input().split()
    s.append([int(TL[0]),int(TL[0])+int(TL[1])+15])

s.sort(key=lambda x:x[0])
# print(s)
ans=0
preend=0
for start,end in s:
    if start>=preend:
        ans+=1
        preend=end
    elif start<preend<=end:
        continue
    elif preend>end:
        preend=end

print(ans)