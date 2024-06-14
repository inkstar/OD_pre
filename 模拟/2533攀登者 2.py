height=list(map(int,input().split(',')))
strength=eval(input())
def climb(mount,direction):
    #找到第一个不是 0的
    j=0
    while (j<len(height) and height[j]!=0):
        j+=1
    cost=0

    for i in range(j+1,len(height)):
        if height[i]==0:
            cost=0
            continue
        diff=height[i]-height[i-1]

        if diff>0:
            cost+=diff*3
            if i+1>=len(height) or height[i]>height[i+1]:
                if cost<strength:
                    if direction:
                        mount.add(i)
                    else:
                        mount.add(len(height)-1-i)
        elif diff<0:
            cost-=diff*3

mount=set()
climb(mount,True)
height.reverse()
climb(mount,False)

print(len(mount))



    

    