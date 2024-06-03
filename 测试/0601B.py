s=list(map(int,input().split(',')))
myans=0
def check(s:list):
    flag=0
    num0=0
    ans=0
    for i in s:
        if flag==0 and i==0:
            num0+=1
        elif flag==0 and i==1:
            ans+=(num0)//2
            num0=0
            flag=1
        elif flag==1 and i==0:
            num0+=1
        elif flag==1 and i==1:
            ans+=(num0-1)//2
            num0=0
    return ans
s2=[]
for i in range(len(s)-1,-1,-1):
    s2.append(s[i])

myans=max(check(s),check(s2))
print(myans)

        

