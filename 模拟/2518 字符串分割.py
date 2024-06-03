K=eval(input())
S=input().split('-')
# print(S)
ans=[]
ans.append(S[0])


def mydeal(s:str):                  #判断和转换大小写，并返回应当 append到 ans的元素
    numa,numA=0,0
    for i in s:
        if 'a'<=i<='z':numa+=1
        elif 'A'<=i<='Z':numA+=1
        else:continue
    if numa>numA:
        return s.lower()
    elif numa<numA:
        return s.upper()
    else:
        # print(s)
        return s
    
def mysplit(s:str):                 #每 K 个字符组团
    i=0
    while i<=len(s)-1:
        ans.append(mydeal(s[i:min(i+K,len(s))]))
        i+=K

t=""
for x in range(1,len(S)):
    t+=S[x]
mysplit(t)
    # print('t ',S[x])
print('-'.join(ans))







