N,M=map(int,input().split())
special=[0]
sample={}
for i in range(N):
    x=eval(input())
    special.append(x)
# print(special)
for i in range(M):
    sample[i+1]=0
    s=list(map(int,input().split()))
    for j in s:
        sample[i+1]+=special[j]
# print(sample)
sample_items=sorted(sample.items(),key=lambda x:(x[1],-x[0]))
# sample_keys=sorted(sample_items,key=lambda x:-x[0])
# print(sample_items)
# print(sample_keys)
for i in range(M-1,-1,-1):
    print(sample_items[i][0])
    