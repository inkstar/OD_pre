s="pwwkew"
i=0
j=1
MaxLen=1
st=[]
st.append(s[0])
k=0
while i<=len(s)-1 and j<=len(s)-1:
    print(i,j,st,MaxLen)
    if s[j] not in st:
        st.append(s[j])
        MaxLen=max(MaxLen,len(st))
        j+=1
        print(i,j,st,MaxLen)
    elif s[j] in st:
        while s[j] in st:
            st.remove(st[k])
            i+=1
        k=0
        st.append(s[j])
        j+=1
        print(i,j,st,MaxLen)
print(MaxLen,st)