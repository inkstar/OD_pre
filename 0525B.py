from collections import Counter
s=list(map(int,input().split(',')))
s_cnt=Counter(s)
print(s_cnt)
st=sorted(s,key=lambda x:(-s_cnt[x],s.index(x)))
print(st)
st_cnt=Counter(st)
ans=[]
for i in st_cnt.keys():
    ans.append(str(i))
print(','.join(ans))



