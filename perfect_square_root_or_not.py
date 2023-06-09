import math
n=int(input())
p=int(math.sqrt(n))
q=p*p
if n==q:
    print("True")
else:
    print("False")