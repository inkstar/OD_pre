N=eval(input())
s=list(map(int,input().split()))
from collections import defaultdict,deque
h=defaultdict(list)
q=deque()
inDegree=[0]*(N+1)
for i in range(0,2*N-1,2):
    h[s[i]].append(s[i+1])
    inDegree[s[i+1]]+=1
ans_list=set(s)
print(inDegree)
print(ans_list)
for i in list(ans_list):
    if inDegree[i]==0:
        q.append(i)
    else:
        ans_list.remove(i)
    # if len(h[i+1])==0:
    #     ans_list.append(i+1)
    # print(h)

while len(q)>0:
    # print(q)
    cnt=q.popleft()
    if len(h[cnt])==0:ans_list.add(cnt)
    for i in h[cnt]:
        inDegree[i]-=1
        if inDegree[i]==0:
            q.append(i)
ans=set(ans_list)
if not all(inDegree):
    print(*ans)
else:
    print(-1)
