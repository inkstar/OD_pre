lst1=input().split(';')
lst2=input().split(';')
dict1={}
dict2={}
for i in lst1:
    classno,grade=i.split(',')
    dict1[classno]=int(grade)
for i in lst2:
    classno,grade=i.split(',')
    dict2[classno]=int(grade)
dictx={}
for i in dict1:
    if i in dict2:
        dictx[i]=dict1[i]+dict2[i]
gradet={}
for i in dictx.keys():
    classt=i[:5]
    if classt not in gradet:
        gradet[classt]=[i]
    else:
        gradet[classt].append(i)
if len(dictx)==0:
    print("NULL")
else:
    for i in sorted(gradet.keys()):
        print(i)
        t=(gradet[i])
        t.sort(key=lambda x:(-dictx[x],x))
        print(';'.join(gradet[i]))
