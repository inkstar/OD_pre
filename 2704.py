s=input().split()
flag=1
dictx={}
for i in s:
    lenx=len(i)
    for j in range(1,lenx):
        if i[:j] not in s:
            flag=0
    if flag==0:
        dictx[i]=0
    else:
        dictx[i]=1
    flag=1
s=sorted(s,reverse=True)
ans=""
for i in s:
    if dictx[i]==1:
        if len(i)>len(ans):
            ans=i
print(ans)
        

        