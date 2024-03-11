N=eval(input())
num=list()
for i in range(N):
    s=eval(input())
    num.append(s)
sort_num=set(num)
s2=sorted(sort_num)
for i in s2:
    print(i)

