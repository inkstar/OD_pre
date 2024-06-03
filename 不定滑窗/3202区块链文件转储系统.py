M=eval(input())
blockchain=list(map(int,input().split()))
ans=0
tmpsum=0
left=0
for i,x in enumerate(blockchain):
    tmpsum+=x
    if tmpsum<=M:
        if tmpsum>ans:
            ans=tmpsum
    else:
        while(tmpsum>M):
            tmpsum-=blockchain[left]
            left+=1
        ans=max(ans,tmpsum)
print(ans)