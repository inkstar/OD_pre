fruits=[1,0,1,4,1,4,1,2,3]
s0=[]
maxx=0
number=0
for i in range(len(fruits)):
    if len(set(s0))<2 and fruits[i] not in s0:
        s0.append(fruits[i])
        number+=1
        maxx=max(maxx,number)
    elif len(set(s0))==2 and fruits[i] not in s0:
        s0.append(fruits[i])
        while len(set(s0))>2:
            s0.remove(s0[0])
            number-=1
        number+=1
        maxx=max(maxx,number)
    elif len(set(s0))<=2 and fruits[i] in s0:
        s0.append(fruits[i])
        number+=1
        maxx=max(maxx,number)
    print(i,s0,fruits[i],maxx,number)
print(maxx,s0)
    

    
