s=input()
stack_bracket=[]
stack_operator=[]
stack_number=[]
signed=1
tmp_num=0
flag_num=0
flag=0
def calcu(ope:str,x:int,y:int):
    if ope=='add':return x+y
    elif ope=='sub':return x-y
    elif ope=='mul':return x*y
    elif ope=='div':return x//y #除零错误在外部处理
i=0
while i<len(s):
    x=s[i]
    if x=='(':
        stack_bracket.append(x)
    elif x==')': #遇到括号开始计算
        #先处理上一个数字
        if '0'<=s[i-1]<='9':
            stack_number.append(signed*tmp_num)
            tmp_num=0
            signed=1

        tmp_ope=stack_operator.pop()
        tmp_y=stack_number.pop()
        tmp_x=stack_number.pop()
        if tmp_ope=='div' and tmp_y==0:
            flag=1
            break    #除零错误
        stack_number.append(calcu(tmp_ope,tmp_x,tmp_y))
        flag_num=0
    elif x in ['m','a','s','d']:
        if x=='m':stack_operator.append('mul')
        elif x=='a':stack_operator.append('add')
        elif x=='s':stack_operator.append('sub')
        elif x=='d':stack_operator.append('div')
        i+=3
        continue
    elif x=='-':signed=-1
    elif '0'<=x<='9':
        tmp_num=tmp_num*10+int(x)
        flag_num=1
    elif flag_num==1 and x==' ' and '0'<=s[i-1]<='9':
        stack_number.append(signed*tmp_num)
        tmp_num=0
        signed=1
        flag_num=0
    i+=1
if flag==0:
    print(stack_number[-1])
else:
    print('error')