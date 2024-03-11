K=input()
boxes=input().split(' ')
flag=0
for i in range(len(boxes)):
    boxes[i]=boxes[i].lower()
    boxes[i]=''.join(filter(str.isalpha,boxes[i]))
    # 只保留一个字符串中所有的字母
    if(set(K)==set(boxes[i])):
        print(i)
        flag=1
        break
if flag==0:       
    print('-1')
# print(boxes)