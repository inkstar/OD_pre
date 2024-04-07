s=input().split()
num=list(int(i) for i in s)
minx=2**17
num.sort()
i=0
j=len(num)-1
print(num)
while(i<j):
    s=num[i]+num[j]
    if s>0:
        if abs(s)<minx:
            minx=abs(s)
            ansx,ansy,anssum=num[i],num[j],abs(s)
            print(ansx,ansy,anssum)
        j=j-1
    elif s<0:
        if abs(s)<minx:
            minx=abs(s)
            ansx,ansy,anssum=num[i],num[j],abs(s)
            print(ansx,ansy,anssum)
        i=i+1
    else:
        ansx,ansy,anssum=num[i],num[j],0
        print(ansx,ansy,anssum)
print(ansx,ansy,anssum)
