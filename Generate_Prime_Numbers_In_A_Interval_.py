import math
def isprime(s):
    p=int(math.sqrt(s))
    if s<2:
        return False
    for i in range(2,p+1):
        if s%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
l=[]

for i in range(n,m+1):
    l.append(i)
for i in l:
    if isprime(i):
       print(i)