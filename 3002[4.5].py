# s=input()
s='asdbuiodevauufgh'
Max=0
ans=0
s0=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in s0:
        ans+=1
        Max=max(ans,Max)
    elif i not in s0:
        ans=0
print(Max)