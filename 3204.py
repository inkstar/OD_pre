s=input()
ls=[]
maxx=0
flag1=0
flag2=0
startx=0
endx=0
for i in range(len(s)):
    if '0'<=s[i]<='9':
        flag1=1
        if s[i-1].isalpha() and s[i+1].isalpha():
            maxx=max(2,maxx)
        elif i==0 or s[i-1].isalpha():
            startx=i
        elif i==len(s)-1 or s[i+1].isalpha():
            endx=i
            if(startx!=endx):
                ls.append([startx,endx])
                maxx=max(endx-startx+2,maxx)
            
    elif s[i].isalpha():
        flag2=1
if(len(ls)>=2):
    for i in range(1,len(ls),1):
        if ls[i][0]-ls[i-1][1]==2:
            maxx=max(ls[i][1]-ls[i-1][0]+1,maxx)
if flag1*flag2==0:
    print(-1)
else:
    print(maxx)
print(ls)



        
