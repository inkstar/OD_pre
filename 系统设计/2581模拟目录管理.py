catalog={}
cnt=''
last=''
def mkdir(s:str):
    global cnt,last
    if s in catalog:
        return
    else:
        catalog[cnt].append(s)
        last=cnt
        cnt=s

def cd(s:str):
    global cnt
    if s in catalog:
        cnt=s
    elif s=='..':
        for i in catalog.keys():
            if catalog[i]==cnt:
                cnt=i
    else:
        return

def pwd():
    print(catalog)

while True:
    try:
        order=input().split()
        if len(order)==1 and order[-1]=='pwd':
            pwd()
        elif len(order)==2 and order[0]=='mkdir':
            mkdir(order[-1])
        elif len(order)==2 and order[0]=='cd':
            cd(order[-1])
    except:
        break