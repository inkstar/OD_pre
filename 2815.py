s=input().split(' ')
counts={}
lst=[]

for i in range(len(s)):
    t=''.join(sorted(list(s[i])))
    counts[t]=counts.get(t,0)+1
    s[i]=''.join(sorted(list(s[i])))

for i in s:
    lst.append((counts[i],len(i),i))

lst.sort(key=lambda x:(-x[0],x[1],x[2]))

print(' '.join(i[2] for i in lst))


