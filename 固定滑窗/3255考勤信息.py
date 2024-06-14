num=eval(input())
data=[]
for i in range(num):
    x=input().split()
    data.append(x)

def check(s:list):
    absent=0
    late=0
    leaveearly=0
    present=0
    if len(s)==1:return 'true'
    s2=sorted(s)
    left=0
    if s2[1]=='absent':return 'false' #条件 1
    for i,x in enumerate(s):
        if i>=1 and s[i][0]=='l' and s[i-1][0]=='l':
            return 'false'            #条件 2
        if x=='present':present+=1
        if i>6 and s[i-7]=='present':present-=1
        if i>=6 and present<=3:return 'false' 
        
    return 'true'

ans=[]
for i in data:
    ans.append(check(i))
print(*ans)