time=input()
ls=[time[0],time[1],time[3],time[4]]
def next_time(s:list):
    TT=int(s[0]+s[1])
    MM=int(s[2]+s[3])
    if MM<59:
        nextTT=TT
        nextMM=MM+1
    elif MM==59:
        if TT<23:
            nextTT=TT+1
            nextMM=0
        elif TT==23:
            nextTT=0
            nextMM=0
    
    newtime=[0]*4
    newtime[0]=str(nextTT//10)
    newtime[1]=str(nextTT%10)
    newtime[2]=str(nextMM//10)
    newtime[3]=str(nextMM%10)
    return newtime
used=set(ls)
while True:
    ls=next_time(ls)
    if all(ch in used for ch in ls):
        s=ls[0]+ls[1]+':'+ls[2]+ls[3]
        print(s)
        break


