def add(n):
    s=0
    while n!=0:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input())
p=add(n)
while True:
    if p<=9:
        print(p)
        break
    else:
        p=add(p)
        