N=eval(input())
words=[]
for i in range(N):
    s=input()
    words.append(s)
chars=input()
def check(x:str):
    color=[0]*128
    for i in x:
        color[ord(i)]+=1
    return color

ans=0
diff=0
cnt_chars=check(chars)
for word in words:
    tmp_cnt=check(word)
    for i in range(128):
        diff+=max(tmp_cnt[i]-cnt_chars[i],0)
    if diff<=cnt_chars[ord('?')]:
        ans+=1
    diff=0
print(ans)