# s1=list(map(int,input().split()))
# s2=list(map(int,input().split()))
s1=[0,5,8,9,9,10]   #black
s2=[5,0,9,9,9,8]
point=[]
go=[[0 for _ in range(19)] for i in range(19)]
for i in range(0,len(s1),2):
    go[s1[i]][s1[i+1]]=1
for i in range(0,len(s2),2):
    go[s2[i]][s2[i+1]]=2

black=0
white=0
for i in range(19):
    for j in range(19):
        if go[i][j]==1:
            if i<18 and go[i+1][j]==0:
                go[i+1][j]=3
                black+=1
            if j<18 and go[i][j+1]==0:
                go[i][j+1]=3
                black+=1
            if i>0 and go[i-1][j]==0:
                go[i-1][j]=3
                black+=1
            if j>0 and go[i][j-1]==0:
                go[i][j-1]=3
                black+=1
for i in range(19):
    for j in range(19):
        if go[i][j]==2:
            if i<18 and (go[i+1][j]==0 or go[i+1][j]==3):
                go[i+1][j]=4
                white+=1
            if j<18 and (go[i][j+1]==0 or go[i][j+1]==3):
                go[i][j+1]=4
                white+=1
            if i>0 and (go[i-1][j]==0 or go[i-1][j]==3):
                go[i-1][j]=4
                white+=1
            if j>0 and (go[i][j-1]==0 or go[i][j-1]==3):
                go[i][j-1]=4
                white+=1
print(black,white)
            





