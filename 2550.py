n=eval(input())
students=[]
height=[]
weight=[]

s1=input().split()
s2=input().split()
for i in range(n):
    height.append(int(s1[i]))
    weight.append(int(s2[i]))

for i in range(n):
    students.append((i+1,height[i],weight[i]))

students.sort(key=lambda x: (x[1], x[2], x[0]))

for i in students:
    print(i[0],end='')