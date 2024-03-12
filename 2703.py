s1=input().split(' ')
s2=input()
s=[]
lenx=len(s2)
for i in s1:
    if i[:(lenx)]==s2:
        s.append(i)
s=sorted(s)
if len(s)==0:
    print(s2)
else:
    print(' '.join(i for i in s))