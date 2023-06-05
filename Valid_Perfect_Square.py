import math
t=int(input())
for i in range(t):
     n=int(input())
     temp=n
     p=int(math.sqrt(temp))
     if p*p==n:
         print("True")
     else:
          print("False")
