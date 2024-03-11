s=input().split(',')
sum=0

for i in s:
    j=int(i)
    sum+=j
s2=str(sum)
s3=list(s2)

print(min(s3))