import math
def perfect(n):
    p=int(math.sqrt(n))
    if p*p==n:
        return True
    else:
        return False
n=int(input())
li=list(map(int,input().split()))
s=0
for i in li:
    if perfect(i):
        s=s+i
print(s)