ratings=[1,2,2]
Candys=[0]*len(ratings)
Candys[0]=1
for i in range(1,len(ratings)):
    if ratings[i-1]>ratings[i]:
        Candys[i]=Candys[i-1]-1
    elif ratings[i-1]<ratings[i]:
        Candys[i]=Candys[i-1]+1
    else:
        Candys[i]=Candys[i-1]-1

Minx=min(Candys)
sum=0
for i in range(len(ratings)):
    Candys[i]+=(1-Minx)
    sum+=Candys[i]
print(sum)


