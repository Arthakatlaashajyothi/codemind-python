import math
def isprime(n):
    if n==1:
        return False
    p=int(math.sqrt(n))
    for i in range(2,p+1):
        if n%i==0:
            return False
    return True
m=int(input())
t=m
rev=0
while m:
    r=m%10
    rev=rev*10+r
    m=m//10
q=rev
if isprime(q) and isprime(t):
    print("circular prime")
elif isprime(t):
    print("prime but not a circular prime")
else:
    print("not prime")