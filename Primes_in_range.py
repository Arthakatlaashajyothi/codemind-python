import math
def isprime(n):
    s=int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,s+1):
        if n%i==0:
            return False
    else:
        return True
m=int(input())
n=int(input())
l=[]
c=0
for i in range(m,n+1):
    l.append(i)
for i in l:
    if isprime(i):
        c=c+1
print(c)
            