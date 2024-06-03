children_list=[]
YN_list=[]
while True:
    try:
        s=input()
        children,YorN=s.split('/')
        children_list.append(int(children))
        YN_list.append(YorN)
    except:
        break
n=len(children_list)
dp=[None]*n
dp[0]=True
for i in range(1,n):
    if YN_list[i]=='Y':
        dp[i]=dp[i-1]
    else:
        dp[i]= not dp[i-1]

class1=[]
class2=[]
for i in range(n):
    if dp[i]:
        class1.append(children_list[i])
    else:
        class2.append(children_list[i])
class1.sort()
class2.sort()
if class2:
    if class1[0]>class2[0]:
        class1,class2=class2,class1
    print(*class1)
    print(*class2)
else:
    print(*class1)



