def well(a:int,b:int):
    return 4*a+3*b+2
def dollar(a:int,b:int):
    return 2*a+b+3
#  i=  71#6
def transf(a:str):
    num1=0
    stack=[]
    flag=0
    if '#' not in a:
        return int(a)
    for i in a:
        if i.isnumeric():
            num1=num1*10+int(i)
        elif i=='#' and flag==0:
            flag=1
            stack.append(num1)
            num1=0
        elif i=='#' and flag==1:
            stack.append(well(stack.pop(),num1))
            num1=0
    stack.append(well(stack.pop(),num1))
    return stack.pop()

s=input()
s1=s.split('$')
print(s1)
stack1=[]
stackans=[]
for i in s1:
    stack1.append(transf(i))
ans=0
print(stack1)
stackans.append(stack1[0])
if len(stack1)>=2:
    for i in stack1[1:]:
        stackans.append(dollar(stackans.pop(),i))
if stackans[-1]<=2**31-1:
    print(stackans[-1])
else:
    print(2**31-1)






