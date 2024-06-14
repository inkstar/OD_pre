from collections import deque
a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))
q=deque()
ans=[]
flag=0
i=0
for i in range(len(a)):
    q.append(a[i])
    while len(q)>0:  
        if q and flag<len(b) and b[flag]==q[0]:
            ans.append('L')
            flag+=1
            q.popleft()
        elif q and flag<len(b) and b[flag]==q[-1]:
            if len(q)!=1:
                ans.append('R')
                flag+=1
                q.pop()
            else:
                ans.append('L')
                flag+=1
                q.popleft()
        else:
            break
print(''.join(ans) if len(ans)==len(a) else 'NO')

