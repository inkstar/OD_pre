n=int(input())
s=list(input())
flag=0
ls=['']*127
num=0
for x,i in enumerate(s):
    if flag==0 and i=='_':
        num+=1
        if num==n:
            ls[num]+='******'
        continue
    elif flag==0 and i=='"':
        flag=1
        if num!=n:
            ls[num]+='"'
    elif flag==1 and i=='"':
        flag=0
        if num!=n:
            ls[num]+='"'
    elif flag==1 and num==n:
        continue
    elif num!=n:
        ls[num]+=i
if n<=num+1:
    print('_'.join(k for k in ls[:(num+1)] if len(k)>0))
else:
    print("ERROR")