costs = [50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58]
k = 7
candidates = 12
lc=len(costs)
i=1
sumx=0
while i<=k:
    if lc>=candidates*2:
        minx=min(costs[0:candidates]+costs[(lc-candidates):lc])
        minx_index=costs.index(minx)
        if minx_index>=candidates and minx_index<lc-candidates:
            minx_index=costs[(lc-candidates):lc].index(minx)+lc-candidates
        sumx+=minx
        print(i,minx,minx_index,sumx,lc)
        del costs[minx_index]
        lc-=1
    else:
        minx=min(costs)
        minx_index=costs.index(minx)
        sumx+=minx
        print(i,minx,minx_index,sumx)
        del costs[minx_index]
        lc-=1
    i+=1
print(sumx)