left=0
right=len(s)-1
flag=0
while left<=right:
    if s[left]==s[right]:
        left+=1
        right-=1
    elif s[left]!=s[right] and flag==0:
        if s[left+1]==s[right]:
            left+=1
            flag=1
        elif s[left]==s[right-1]:
            right-=1
            flag=1
        else:
            return False
    elif s[left]!=s[right] and flag==1:
        return False
return True