L1,L2=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
# print(L1,L2,l1,l2)
if sum(l1)>sum(l2):
    minus=sum(l1)-sum(l2)
    l1.sort()
    for i in l1:
        if (i+minus//2) in l2:
            print(i,i-minus//2)
            break
elif sum(l1)<sum(l2):
    minus=sum(l2)-sum(l1)
    l1.sort()
    for i in l1:
        if (i+(minus//2)) in l2:
            print(i,i+(minus//2))
            break