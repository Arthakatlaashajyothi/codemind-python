n=int(input())
p=0
q=1
print(p,end=" ")
print(q,end=" ")
c=0
while c<(n-2):
    m=p+q
    print(m,end=" ")
    c=c+1
    p=q
    q=m
    