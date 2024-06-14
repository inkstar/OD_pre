#系统设计 2580
m=eval(input())
n=eval(input())
File={}
reFile={}
accesstime=0
def Put(a:str,b:str):
    global m
    fileName=a
    fileSize=int(b)
    recent_time=0   #最近访问时间
    total_time=0    #总访问次数
    if m-fileSize>=0:
        m-=fileSize
        File[fileName]=[fileName,fileSize,recent_time,total_time]
        reFile[recent_time]=fileName
    else:
        while m-fileSize<0:         #内存不够的时候要处理
            sortedfile=list(File.values())
            sortedfile.sort(key=lambda x:(x[3],x[2]))
            first_key=sortedfile[0][0]
            m+=sortedfile[0][1]
            del File[first_key]
        m-=fileSize
        File[fileName]=[fileName,fileSize,recent_time,total_time]
        reFile[recent_time]=fileName
def Get(a:str):
    global accesstime
    fileName=a
    if fileName in File.keys():
        accesstime+=1
        File[fileName][2]=accesstime
        File[fileName][3]+=1
        

while(True):
    try:
        s=input().split()
        if s[0]=="put":
            Put(s[1],s[2])
        elif s[0]=="get":
            Get(s[1])
    except:
        break

sortedfile=list(File.values())
if len(sortedfile)>0:
    print(','.join(sortedfile[i][0] for i in range(len(sortedfile))))
else:
    print("NONE")
