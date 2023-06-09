import math
def isprime(n):
    p=int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,p+1):
        if n%i==0:
            return False
    return True
s=int(input())
for i in range(s):
    if isprime(s):
        print("prime")
        break
else:
    print("not a prime")