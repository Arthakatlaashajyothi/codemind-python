def next(n):
    while  True:
        for i in range(2,n):
            if n%i==0:
                break
        else:
             return n
        n=n+1
def previous(n):
    while  True:
        for i in range(2,n):
            if n%i==0:
                break
        else:
             return n
        n=n-1
t=int(input())
for i in range(t):
    m=int(input())
    k=abs(m-next(m))
    h=abs(m-previous(m))
    if k<h:
        print(next(m))
    else:
        print(previous(m))
    