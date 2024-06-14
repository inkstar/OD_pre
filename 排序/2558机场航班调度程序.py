airport=list(map(str,input().split(',')))
s=[]
for i in range(len(airport)):
    s.append((airport[i],airport[i][0:2],airport[i][2:6]))
print(s)
s.sort(key=lambda x:(x[1],x[2]))
print(','.join(s[i][0] for i in range(len(airport))))