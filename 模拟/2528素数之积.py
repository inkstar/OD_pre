from math import sqrt
from functools import cache
num=eval(input())
flag=0
prime=[2,3,5,7]
@cache
def is_prime(x:int):
    if x in prime:return True
    if x%2==0:return False
    for i in range(3,int(sqrt(x))+1):
        if x%i==0:return False
    prime.append(x)
    return True

for i in range(2,int(sqrt(num)+1)):
    if num%i==0 and is_prime(i) and is_prime(num//i):
        print(i,num//i)
        flag=1
        break
if flag==0:
    print("-1 -1")
    