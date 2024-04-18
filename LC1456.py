s='leetcode'
vow=['a','e','i','o','u']
k=3
num=0
maxx=0
left=0
for i in range(k):
    if s[i] in vow:
        num+=1
maxx=num
print(maxx)
for i in range(k,len(s),1):
    if s[i] in vow and s[i-k] in vow:
        print(i,s[i],s[i-k],num,maxx)
        continue
    elif s[i] in vow and s[i-k] not in vow:
        num+=1
        maxx=max(num,maxx)
    elif s[i] not in vow and s[i-k] in vow:
        num-1
    else:
        print(i,s[i],s[i-k],num,maxx)
        continue
    print(i,s[i],s[i-k],num,maxx)
print(maxx)