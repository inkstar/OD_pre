S=input()
L=input()

i=0
j=0
LastPosition=-1
number=0
while i<=len(S)-1 and j<=len(L)-1:
    if S[i]==L[j]:
        LastPosition=j
        i+=1
        j+=1
        number+=1
    elif S[i]!=L[j]:
        j+=1
if number!=len(S):
    print(-1)
else:
    print(LastPosition)

