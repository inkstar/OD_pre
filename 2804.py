N=eval(input())
Max=-1
s=[]
for i in range(N):
    a=eval(input())
    if a in s:
        Max1=i-s.index(a)
        if Max1 > Max:
            Max=Max1
    s.append(a)
print(Max)