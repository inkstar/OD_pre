gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
sum1=sum(gas)
sum2=sum(cost)
if sum1<sum2:
    print(-1)
else:
    currentgas=0
    currentcost=0
    currentstart=0
    flag=0
    i=0
    failure=0
    while(flag<=len(gas)):
        currentcost=cost[i]
        currentgas+=gas[i]-cost[i]
        if currentgas<0:
            currentstart+=1
            currentgas=0
            currentcost=0
            flag=0
            failure+=1
            if failure==len(gas):
                print(-1)
            i=currentstart
        else:
            flag+=1
            i+=1
            i=i%len(gas)
            if flag==len(gas):
                print(currentstart)

        