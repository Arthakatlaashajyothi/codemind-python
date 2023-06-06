n=int(input())
temp=n
rev=0
n=(abs(n))
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp<0:
    print("-%d"%rev)
else:
    print(rev)