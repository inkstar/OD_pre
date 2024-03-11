s=input().split(' ')
for i in range(s):
    # i=''.join(sorted(i))
    s[i]=''.join(sorted(s[i]))
print(s)
