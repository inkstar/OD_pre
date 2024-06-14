from collections import Counter
s=input()
s2=s*2
n=len(s)
def check(x:str):
    n=Counter(x)
    if(n['l'])%2==0 and n['o']%2==0 and n['x']%2==0:
        return True
    else:
        return False
left=0
right=left+1
ans=0
while left<=n and right<=2*n-1:
    if right-left+1>n:
        left+=1
        right=left+1
        continue
    elif right-left+1<=n:
        if check(s2[left:(right+1)]):
            ans=max(ans,right-left+1)
        right+=1
print(ans)

