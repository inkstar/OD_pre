employee=[]
while True:
    try:
        x,y=map(int,input().split())
        employee.append((x,y))
    except:
        break
employee.sort(key=lambda x:(-x[0],-x[1]))
print("answer")
for i in range(10):
    print(employee[i][0],employee[i][1])