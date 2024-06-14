s=list(map(int,input().split(',')))
energy=eval(input())
res=0
s1=[]
s2=[]
s1.append(0)
anspoint=[]
for i in range(1,len(s)):
    s1.append(s[i]-s[i-1])
for j in range(0,len(s)-1):
    s2.append(s[j]-s[j+1])
s2.append(0)
ans=[]
if s[0]>s[1]:
    ans.append(s[0])
    anspoint.append(0)
for i in range(len(s)):
    if s1[i]>0 and s2[i]>0:
        ans.append(s[i])
        anspoint.append(i)
if s[-1]>s[-2]:
    ans.append(s[-1])
    anspoint.append(len(s)-1)
anspoint.sort()
for i in ans:
    if energy>=i*3:res+=1
# print(res)
###此处res满足70%答案
#处理上坡
#从左到右
s3=[]
for i in range(len(s1)):
    if s1[i]<0:
        s3.append(-s1[i])
    else:
        s3.append(s1[i])
#从右到左
s4=s2
for i in range(len(s2)):
    if s2[i]<0:
        s4[i]=-s2[i]
    else:
        s4[i]=s2[i]
#
print(s3)
print(s4)
# 上下坡加起来
res2=[]
tmp_sum=0
flag_cal=0
while flag_cal<len(ans):
    target=anspoint[flag_cal]
    for i in range(target,-1,-1):
        if s[i]!=0:
            tmp_sum+=s3[i]
        elif s[i]==0:
            res2.append(3*tmp_sum)
            tmp_sum=0
            flag_cal+=1
            break
print('test',res2)
res3=[]
tmp_sum=0
flag_cal=0
while flag_cal<len(ans):
    target=anspoint[flag_cal]
    for i in range(target,len(s)):
        if s[i]!=0:
            tmp_sum+=s4[i]
        elif s[i]==0:
            res3.append(3*tmp_sum)
            tmp_sum=0
            flag_cal+=1
            break

# res3.reverse()
print('test',res3)
# print(res2)
# print(res3)
# 最后答案的计算
resfinal=res3
finalans=0
for i in range(len(ans)):
    resfinal[i]=min(res2[i],res3[i])
    if resfinal[i]<=energy:finalans+=1
print(finalans)
