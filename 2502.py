s=input()
stack=[]
digit=0
last=''
flag=0
for x,i in enumerate(s):
    if i.isnumeric() and x!=len(s)-1:
        digit=digit*10+int(i)
    elif i.isalpha():
        if digit>2:
            stack.append(digit*i)
            digit=0
        elif 0<digit<=2:
            print('!error')
            flag=1
            break
        elif ((x>1 and s[x]==s[x-1]) and (s[x-1]==s[x-2])):
            print(x,i,s[x],s[x-1],s[x-2])
            print('!error')
            flag=1
            break
        elif (x>1 and s[x]==s[x-1] and s[x-2].isnumeric()):
            print('!error')
            flag=1
            break
        else:
            stack.append(i)
    elif i.isnumeric()==False and i.isalpha()==False:
            print('!error')
            flag=1
            break
    elif i.isnumeric() and x==len(s)-1:
        print('!error')
        flag=1
        break
if flag==0:
    print(''.join(stack))

