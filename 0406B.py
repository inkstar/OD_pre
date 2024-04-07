s=input().split()
ls=[]
sums=[]
mums=[]
for i in range(0,len(s),2):
    ls.append([int(s[i]),int(s[i+1])])
    sums.append(int(s[i])+int(s[i+1]))
    mums.append(abs(int(s[i])-int(s[i+1])))
print(s)
print(ls)
print(sums)
flag=[1]*len(sums)
for i in range(1,len(sums)-1):
    if sums[i]==sums[i-1] and sums[i]==sums[i+1]:
        flag[i]=0
    if ls[i][0]==ls[i-1][0] and ls[i][0]==ls[i+1][0]:
        flag[i]=0
    if ls[i][1]==ls[i-1][1] and ls[i][1]==ls[i+1][1]:
        flag[i]=0
    if mums[i]==mums[i-1] and mums[i]==mums[i+1]:
        flag[i]=0
ans=[]
for i in range(len(sums)):
    if flag[i]==1:
        ans.append(ls[i][0])
        ans.append(ls[i][1])


print(flag)
for i in ans:
    print(i,end=' ')
    
    