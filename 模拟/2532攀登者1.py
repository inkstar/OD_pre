s=list(map(int,input().split(',')))
energy=eval(input())
res=0
s1=[]
s2=[]
s1.append(0)
for i in range(1,len(s)):
    s1.append(s[i]-s[i-1])
for j in range(0,len(s)-1):
    s2.append(s[j]-s[j+1])
s2.append(0)
ans=[]
s3=[0]*len(s)
for i in range(1,len(s)-1):
    if ((s1[i]>0 and s2[i]<0)or (s1[i]<0 and s2[i]>0) )and s[i]!=0:
        s3[i]=-1
for i in range(1,len(s)-1):
    if s1[i]>0 and s2[i]>0 and s3[i-1]+s3[i+1]!=-2:
        ans.append(s[i])
if s[0]>s[1]:ans.append(s[0])
if s[-1]>s[-2]:ans.append(s[-1])
for i in ans:
    if energy>=i*3:res+=1
#此处print res可获得70分
print(res)


