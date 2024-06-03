n=eval(input())
energy=list(map(int,input().split()))
MinEnergy=eval(input())
# print(pop)
# print(energy)
TeamNum=0
energy.sort()
left=0
right=n-1
if energy[0]>=MinEnergy:
    print(n)
else:
    while left<right:
        if energy[right]>=MinEnergy:
            TeamNum+=1
            right-=1
        elif energy[left]+energy[right]>=MinEnergy:
            TeamNum+=1
            right-=1
            left+=1
        else:
            left+=1
    print(TeamNum)