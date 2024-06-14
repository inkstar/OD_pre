s=list(map(int,input().split(',')))
s2=[(x,abs(x)%10,i) for i,x in enumerate(s)]
s2.sort(key=lambda x:(x[1],x[2]))

result=','.join(str(s2[i][0]) for i in range(len(s2)))
print(result)