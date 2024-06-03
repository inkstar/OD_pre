K=eval(input())
S=input()
new_s=['']*(len(S)**2)

num=0
k=0
t=0
while S[t]!='-':
    new_s[0]+=S[t]
    t+=1
new_s[0]+='-'
num+=1
for i in range(t+1,len(S)):
    if S[i]!='-' and k!=K:
        new_s[num]+=S[i]
        k+=1
        print('1',i,k,num,S[i],new_s)
    elif S[i]!='-' and k==K:
        new_s[num]+='-'
        num+=1
        new_s[num]+=S[i]
        k=1
        print('2',i,k,num,S[i],new_s)
    elif S[i]=='-' and (k==0 or k==K):
        print('3',i,k,num,S[i],new_s)
        continue
    elif S[i]=='-' and k!=K and k!=0:
        k=0
        num+=1
        print('4',i,k,num,S[i],new_s)
    else:
        new_s[num]+=S[i]
        k+=1
        print('5',i,k,num,S[i],new_s)




# print(new_s[:num+1],num)
abc_num=0
ABC_num=0
for i in range(1,len(new_s)):
    for j in new_s[i]:
        if 'a'<=j<='z':
            abc_num+=1
        elif 'A'<=j<='Z':
            ABC_num+=1
    if abc_num>ABC_num:
        new_s[i]=new_s[i].lower()
        abc_num=0
        ABC_num=0
    elif abc_num<ABC_num:
        new_s[i]=new_s[i].upper()
        abc_num=0
        ABC_num=0   
print(''.join(new_s[:len(new_s)]))


