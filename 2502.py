s=list(input())
count=0
st=set()
ls=[]
for i in range(len(s)):
    if i==0:
        st.add(s[i])
        count+=1
    elif s[i]==s[i-1]:
        count+=1
    elif s[i]!=s[i-1]:
        if count>2:
            ls.append(str(count)+s[i-1])
        elif count<=2:
            ls.append(count*s[i-1])
        count=1
    else:
        count+=1
    if i==len(s)-1:
        ls.append(count*s[i])
print(ls)
    
