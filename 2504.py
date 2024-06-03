s=input()
flag=0          #记录开始和结束记录坐标
flag1=0         #记录逗号
flag_law=0      #记录合法性个数 
num_law=0   
digit=0
L,R=0,0
distance_max=0
distance=0     
point=[(0,0)]

for x,i in enumerate(s):
    print(x,s[x],flag)
    if s[x]=='(':
        flag=1
        print(x,s[x],flag,flag_law,digit,point)
    elif flag==1 and i.isnumeric() and flag_law==0:
        if i=='0' and s[x-1]=='(':           
            flag_law=1
            num_law+=1
        elif i=='0' and s[x-1]==',':
            flag_law=1
            num_law+=1
        elif flag_law!=1:
            digit=digit*10+int(i)
        print(x,s[x],flag,flag_law,digit,point)
    elif flag==1 and i==',' and flag_law==0:
        flag1=1
        if flag_law==1:
            continue
        elif flag_law==0:
            L=digit
            digit=0
        print(x,s[x],flag,flag_law,digit,point)
    elif flag==1 and i==')':
        if flag1==1:
            R=digit
            digit=0
            distance=L*L+R*R
            flag1=0
            if distance>distance_max and flag_law==0:
                if len(point)>0:
                    point.pop()
                point.append((L,R))
                distance_max=distance
            flag_law=0
            flag=0
            print(x,s[x],flag,flag_law,digit,point)
        elif flag1==0:
            flag_law=0
            flag=0
            digit=0
    elif flag==1 and i.isnumeric()==False and i!=',' and i!=')' and flag_law==0:
        flag_law=1
        print('shit')
        print(x,s[x],flag,flag_law,digit,point)
    elif i==',':
        flag1=1
    else:
        continue
ans='('+str(point[0][0])+','+str(point[0][1])+')'
print(ans)






