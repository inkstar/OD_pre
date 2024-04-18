s=input().split(',')
s.sort(key=lambda x:(x+(6-len(x))*x[-1]),reverse=True)
print(''.join(s))
