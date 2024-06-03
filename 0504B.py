n,m=map(int,input().split())
subject=input().split()
score=[]
for i in range(n):
    s=input().split()
    score.append([s[0]])
    for j in range(1,m+1):
        score[i].append(int(s[j]))
try:
    test=input()
    # print(score)
    testno=subject.index(test)+1
    # print(testno)
    score.sort(key=lambda x:(-x[testno],x[0]))
    ans=[]
    for j in range(n):
        ans.append(score[j][0])
    print(testno)
    print(*ans)
except:
    for j in range(n):
        score[j].append(sum(score[j][1:]))
    print(score)
    score.sort(key=lambda x:(-x[-1],x[0]))
    ans=[]
    for j in range(n):
        ans.append(score[j][0])
    print(*ans)


