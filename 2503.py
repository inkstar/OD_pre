n=int(input())
str=[]
a=[0]*51
a[0],a[1],a[2]=1,2,4
# print(a)
for i in range(3,51):
    a[i]+=(a[i-1]+a[i-2]+a[i-3])
# print(a)  
for i in range(n):
    x=input()
    x2=''
    for j,t in enumerate(x):
        if ord(t)+a[j]<=122:
            x2+=chr(ord(t)+a[j])
            print('1',j,t,chr(ord(t)+a[j]),ord(t)+a[j],t,a[j],j)
        else:
            if (ord(t)+a[j]-96)%26!=0:
                x2+=chr(((ord(t)+a[j]-96)%26+96))
            else:
                x2+='z'
            
    str.append(x2)
    
for i in range(n):
    print(str[i])
